import threading
import time
from random import randint

class SerialRead(threading.Thread):
    def __init__(self,dataClass, mainPage):
        self.mainPageRefference = mainPage
        threading.Thread.__init__(self)

        self._dataClass = dataClass
    
    def run(self):
        while True:
            if self.mainPageRefference.shouldSerialReadFunc():
                #print("updating data")
                self._dataClass.XData.append(self._dataClass.XData[-1] + 1)
                self._dataClass.YData.append(randint(0,256))
                time.sleep(0.1)