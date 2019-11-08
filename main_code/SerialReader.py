import threading
import time
from random import randint

import serial.tools.list_ports
import serial
import tkinter as ttk
from tkinter.ttk import Combobox

class SerialRead(threading.Thread):
    def __init__(self,dataClass, parent):


        self.port = ""
        
        self.ser = None

        self.parent = parent 
       
        #self.openSerial()

        self.lineArray = []

        self.mainPageRefference = None
        threading.Thread.__init__(self)

        self._dataClass = dataClass
    
        self.line = ""
        if False:
            for x in self._dataClass:
                for i in [1.1,2,3,3,5,6]:
                    x.XData.append(i)
                    x.YData.append(i+1)
            

    def openSerial(self):
        ports = list(serial.tools.list_ports.comports(include_links=False))
        ports_array = []

        for p in ports:
            ports_array.append(str(p).split(" ")[0])
        if len(ports) == 0:
           self. parent.printToConsole("No com ports were found\n",False)
        elif len(ports) > 1:  #če je več com portov se odpre dialog za izbiro
            top = ttk.Toplevel()
            top.title("Choose a COM port")
            msg = ttk.Message(top, text="Choose a COM port out of the following:")
            msg.pack()

            comportSelectionComboBox = Combobox(top,values=ports_array,state="readonly")
            comportSelectionComboBox.pack()

            button = ttk.Button(top, text="continue",command=lambda:self.setComPort(comportSelectionComboBox,top))
            button.pack()
        elif len(ports) == 1:
            self.port = ports_array[0]
            self.ser = serial.Serial(self.port,38400)
            self.parent.printToConsole("Serial connection opened \n" if self.ser.isOpen() else "Serial connection not opened \n",False)
            #print(self.ser.isOpen())

    def closeSerialConnection(self):
        if self.ser:
            self.ser.close()
        #print(self.ser)

    def setComPort(self, combobox,top):
        print(combobox.get())
        self.port = combobox.get()
        self.ser = serial.Serial(self.port,9600)
        print(self.ser.isOpen())
        top.destroy()


    def run(self):
        try:
            prev = False
            #sizeOfArr = 1
            shouldCalcDiff = False
            diff = 0
            strToPrint = ""
            counter1 = 0
            #time.sleep(0.1)
            while True:
                #time.sleep(0.01)
                shouldRead = self.mainPageRefference.shouldSerialReadFunc()
                if not shouldRead == prev: #če pride do spremembe state-a (pauza, zdaj) serial branja pol pobriše srial input ap zračuna difference cajta k se spet zalaufa read
                    if self.ser: 
                        self.ser.flushInput()
                        self.ser.read()
                    prev = shouldRead
                    shouldCalcDiff = True
                    passOne = True

                if shouldRead:
                    timeArd = 0
                    if not self.ser: break
                    if not self.ser.isOpen() : break
                    try:                        
                        inputChar = self.ser.read().decode("utf-8")
                    except serial.serialutil.SerialException:
                        self.parent.printToConsole("Lost serial connection\n",False)
                        break
                    except:
                        self.parent.printToConsole("Something unexpected happened to serial connection.\n",False)
                        break
                    if inputChar != "\n":
                        self.line += inputChar
                    else:
                        self.lineArray = self.line.strip().split("\t")
                        
                        strToPrint += str(self.lineArray)
                        strToPrint += "\n"
                        if counter1 > 10:
                            self.parent.printToConsole(strToPrint,True)
                            strToPrint = ""
                            counter1 = 0
                        counter1 += 1
                        #print(self.lineArray)
                        try:
                            timeArd = float(self.lineArray[0])
                        except:
                            self.parent.printToConsole("Problem with conversion to float\n",False)
                            #print("problem with conversion to float")
                        self.line = ""

                        if self._dataClass:
                            if shouldCalcDiff:
                                if passOne:
                                    passOne = False
                                    print("Pass one")
                                    pass
                                else:
                                    #print(self._dataClass[0].XData[-1])
                                    #print(self._dataClass[0].XData)
                                    if self._dataClass[0].XData[-1]:
                                        print("self._dataClass[0].XData[-1] obviously exists")
                                        diff = timeArd - self._dataClass[0].XData[-1]
                                    shouldCalcDiff = False
                                    passOne = False
        
                            else:
                                for x in range(1,len(self.lineArray)):
                                    if self._dataClass[x-1] and self.lineArray[x]:
                                        self._dataClass[x-1].XData.append(timeArd-diff)
                                        self._dataClass[x-1].YData.append(self.lineArray[x])
               
                else:
                    time.sleep(0.01)
                    pass

        
        except Exception as e:

            print("exception on serial reader therad run")            
            print(e)
