import serial
import random

class serialReader():
    def __init__(self, parent, nrOfLines):
        self.serialConn = None
        self.console = parent.consoleController
        self.prevStr = ""
        self.nrOfLines = nrOfLines
        print("NrOfLines: "+str(nrOfLines))

    def openSerialConnection(self, comPort, baudrate):
        self.serialConn = serial.Serial(comPort, baudrate)
        if self.serialConn.isOpen():
            self.console.printToRightConsole("Opening serial connection @ " + str(comPort) + ", baudrate : " + str(baudrate))
        else:
            self.console.printToRightConsole("Couldn't open serial connection")


    def closeSerialConnection(self):
        pass

    def readSerialBuffer(self):
        print("reading serial buffer")
        if not self.serialConn.isOpen(): return []
        rawInputString = ""
        timeArr = []
        yDataToReturn = []

        while self.serialConn.in_waiting > 0:
            inputByte = self.serialConn.read()
            try:rawInputString += inputByte.decode("utf-8")
            except:self.console.printToRightConsole("Couldn't decode received data")
        

        #print(rawInputString.strip().split("\t")) 
        print("prevStr: "+self.prevStr)
        tempStr = self.prevStr
        for char in rawInputString:
            if char != "\n":
                tempStr += char
            else:
                inputArr = tempStr.strip().split("\t")
                tempStr = ""
                print(inputArr)
                if len(inputArr) != self.nrOfLines+1:
                    pass
        self.prevStr = tempStr
        #print(tempStr)
                    


        """
        oneDataInput_String = ""

        oneDataInput_String += self.prevStr

        for char in rawInputString:
            if char == "\n":
                inputArr = oneDataInput_String.strip().split("\t")
                #print(nekineki)
                try:time = float(inputArr[0])
                except:return
                timeArr.append(time)
                others = inputArr[1:]
                yDataToReturn.append(others)
                #print(others)
                #print(time)
                #return [others], time
                oneDataInput_String = ""
            else:
                oneDataInput_String += char

        #print(yDataToReturn)
        #print(timeArr)
        if len(yDataToReturn) > 0:    
            print(len(yDataToReturn[-1]))
            if len(yDataToReturn[-1]) != self.nrOfLines:
                self.prevStr = "".join(str(i) for i in inputArr[-1])
                yDataToReturn[-1] = None
"""
        arrToReturn = [yDataToReturn, timeArr]
        #print(yDataToReturn)
        #print(timeArr)
        
        #print(arrToReturn)

        #print(len(yDataToReturn))
        #print(len(timeArr))

        return arrToReturn
       # return [[1,random.randint(1,5)],[random.randint(1,10),random.randint(1,10)],[1,2],[1,2],[1,2]], [time, time+1]



