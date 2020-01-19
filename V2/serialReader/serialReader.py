import serial
import random

class serialReader():
    def __init__(self, parent, nrOfLines):
        self.serialConn = None
        self.parent = parent
        self.console = parent.consoleController
        self.prevStr = ""
        self.nrOfLines = nrOfLines
       # print("NrOfLines: "+str(nrOfLines))

    def openSerialConnection(self, comPort, baudrate):
        #self.serialConn = serial.Serial(comPort, baudrate)

        self.serialConn = serial.Serial()
        self.serialConn.port = comPort
        self.serialConn.baudrate = baudrate
        self.serialConn.setDTR(False)
        self.serialConn.open()

        if self.serialConn.isOpen():
            self.console.printToRightConsole("Opening serial connection @ " + str(comPort) + ", baudrate : " + str(baudrate))
        else:
            self.console.printToRightConsole("Couldn't open serial connection")


    def closeSerialConnection(self):
        self.serialConn.close()
        pass

    def readSerialBuffer(self):
        #print("reading serial buffer")


        if not self.serialConn.isOpen(): 
            #self.parent.changeReadingFromSerialState()
            self.parent.animationFunc.event_source.stop()
            self.parent.readingFromSerialState = False
            self.console.printToRightConsole("Serial connection not open, pausing serial reader")
            return []

        #self.prevStr = ""
        #self.serialConn.flush()

        rawInputString = ""
        timeArr = []
        yDataToReturn = []

        while self.serialConn.in_waiting > 0:
            inputByte = self.serialConn.read()
            try:rawInputString += inputByte.decode("utf-8")
            except:self.console.printToRightConsole("Couldn't decode received data")
        

        #print("prevStr: "+self.prevStr) 
        tempStr = self.prevStr
        timeArr = []
        yDataToReturn = []
        for char in rawInputString:
            if char != "\n":
                tempStr += char
            else:
                inputArr = tempStr.strip().split("\t")
                tempStr = ""
                #print(inputArr)
                if len(inputArr) < self.nrOfLines+1:
                    #print(inputArr)
                    #print("len(inputArr) != self.nrOfLines+1")
                    pass
                else:
                    time = inputArr[0]
                    yData = inputArr[1:]
                    #print(time, yData)
                    yDataToReturn.append(yData)
                    timeArr.append(time)
        self.prevStr = tempStr
        #print(tempStr)
                    

        arrToReturn = [yDataToReturn, timeArr]
        #print(arrToReturn)
        return arrToReturn


