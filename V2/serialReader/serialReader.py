import serial
import random
import time

class serialReader():
    def __init__(self, parent, nrOfLines):
        self.serialConn = None
        self.parent = parent
        self.console = parent.consoleController
        self.prevStr = ""
        self.nrOfLines = nrOfLines
        self.prevTime = 0
        self.shouldCalcTimeDiff = False
        self.timeDiff = 0
        self.firstTime = True
        self.initialTimeDiff = 0

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

    def clearSerialBuffer(self):
        while self.serialConn.in_waiting > 0:
            self.serialConn.read()
        self.prevStr = ""

    def setPrevTime(self, time):
        self.prevTime = time

    def readSerialBuffer(self):
        #print("reading serial buffer")

        if not self.serialConn.isOpen(): 
            self.parent.animationFunc.event_source.stop()
            self.parent.readingFromSerialState = False
            self.console.printToRightConsole("Serial connection not open, pausing serial reader")
            return []

        rawInputString = ""
        timeArr = []
        yDataToReturn = []


        while self.serialConn.in_waiting > 0:
            inputByte = self.serialConn.read()
            try:rawInputString += inputByte.decode("utf-8")
            except:self.console.printToRightConsole("Couldn't decode received data")



        tempStr = self.prevStr
        timeArr = []
        yDataToReturn = []

        for char in rawInputString:
            if char != "\n":
                tempStr += char
            else:
                inputArr = tempStr.strip().split("\t")
                tempStr = ""
                print(inputArr)
                if len(inputArr) < self.nrOfLines+1:
                    pass
                else:

                    if self.firstTime: #če se prvič izvede tale rutina in arduino pač ne pošiljša številk od nule, se prvič time diff nastavi kar na prejeto vrednost časa (da se jo potem odšteje/ nastavi kot offset)
                        self.timeDiff = float(inputArr[0])
                        #print("first time time diff %d" % self.timeDiff)
                        self.firstTime = False

                    elif self.shouldCalcTimeDiff: 
                        temp = self.timeDiff
                        self.timeDiff = (float(inputArr[0]) - float(self.prevTime))
                        if self.timeDiff - temp < 0:
                            print("dfghjklčć",self.timeDiff - temp)
                            self.timeDiff = temp
                            return []
                        #print("self.timeDiff += (float(inputArr[0]) - float(self.prevTime)) : %3d += (%3d - %3d)" % (float(self.timeDiff), float(inputArr[0]), float(self.prevTime)))
                        self.shouldCalcTimeDiff = False
                        #print(self.timeDiff, inputArr[0], self.prevTime)

                    timeVal = float(inputArr[0]) - self.timeDiff
                    yData = inputArr[1:]
                    yDataToReturn.append(yData)
                    timeArr.append(timeVal)
        self.prevStr = tempStr
        #print(tempStr)
                    

        arrToReturn = [yDataToReturn, timeArr]
        #print(arrToReturn)
        return arrToReturn


