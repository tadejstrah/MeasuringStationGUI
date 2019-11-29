import serial
import random

class serialReader():
    def __init__(self):
        self.serialConn = None
        

    def openSerialConnection(self, comPort, baudrate):
        #print(comPort)
        self.serialConn = serial.Serial(comPort, baudrate)
        #print(self.serialConn.isOpen())


    def closeSerialConnection(self):
        pass


    def readSerialBuffer(self):
        if not self.serialConn.isOpen(): return []
        #print(self.serialConn.in_waiting)
        string = ""
        time = 5
        while self.serialConn.in_waiting > 0:
            inputByte = self.serialConn.read()
            try:string += inputByte.decode("utf-8")
            except:pass
            neki = ""
        for char in string:
            if char == "\n":
                nekineki = neki.strip().split("\t")
                #print(nekineki)
                #time = float(nekineki[0])
                others = nekineki[1:]
                print(others)
                print(time)
                #return [others], time
                neki = ""
            else:
                neki += char
        #print(string.strip().split("\t"))
        string = ""
        return [[1,random.randint(1,5)],[random.randint(1,10),random.randint(1,10)],[1,2],[1,2],[1,2]], time



