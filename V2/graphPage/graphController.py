import graphPage.graphLine
import defaults

import serial.tools.list_ports
import tkinter as tk
from tkinter.ttk import Combobox

from serialReader import serialReader

import threading
from matplotlib.animation import FuncAnimation

from time import sleep

import easygui
from datetime import datetime

class graphController():
    def __init__(self, view, parent):
        self.view = view
        view.controller = self
        self.consoleController = parent.getControllerRefferenceOf("console")
        self.rawLineData = []
        self.data = []
        self.parent = parent
        self.serialReader = None
 
        self.readingFromSerialState = True


    def getComPort(self):
        ports = list(serial.tools.list_ports.comports(include_links=False))
        ports_array = []

        for p in ports:
            ports_array.append(str(p).split(" ")[0])
        if len(ports) == 0:
            self.consoleController.printToRightConsole("No COM ports were found")
        elif len(ports) > 1:  #če je več com portov se odpre dialog za izbiro
            top = tk.Toplevel()
            top.title("Choose a COM port")
            msg = tk.Message(top, text="Choose a COM port out of the following:")
            msg.pack()

            comportSelectionComboBox = Combobox(top,values=ports_array,state="readonly")
            comportSelectionComboBox.pack()

            port = tk.StringVar()
            button = tk.Button(top, text="continue",command=lambda:[port.set(comportSelectionComboBox.get()), top.destroy()])
            
            button.pack()
            button.wait_variable(port)
            port = port.get()
            self.consoleController.printToRightConsole("You chose the following comport: "+ port)
            return port
        
        elif len(ports) == 1:
            self.consoleController.printToRightConsole(ports_array[0] + " found")
            return ports_array[0]


    def setData(self, data, **kwargs):
        self.rawLineData = data[0]
        self.view.draw()

        if "values" in kwargs.keys():
            #pass
            #print(kwargs["values"])
            temp = []

            nrOfLines = len(kwargs["values"][0])
            for index, value in enumerate(kwargs["values"][0][0]):
                temp.append([kwargs["values"][0][i][index] for i in range(nrOfLines)])


            time = kwargs["values"][1]
            #print(values)
            #print(time)
            self.view.updateGraph([temp, time])


        self.baudrate = data[1]
        self.openSerialConnection(self.baudrate)


        if self.serialReader == None:
            print("serialReader = None")
            return
            
        if "values" not in kwargs.keys():
            #print("values not in kwargs")
            self.animationFunc = FuncAnimation(self.view.fig, lambda x:self.view.updateGraph(self.serialReader.readSerialBuffer()), interval=defaults.refreshRate, repeat=True, repeat_delay=defaults.animationRefreshRate)



    def openSerialConnection(self, baudrate):
        self.comport = self.getComPort()

        if self.comport == None: return #če ne najde comporta ne nardi nič naprej
        self.serialReader = serialReader.serialReader(self, len(self.data))
        self.serialReader.openSerialConnection(self.comport, baudrate)

    def changeReadingFromSerialState(self):
        if not self.readingFromSerialState:
            self.serialReader.clearSerialBuffer()
            self.serialReader.setPrevTime(self.view.getLastTimeValue())
            self.serialReader.shouldCalcTimeDiff = True

            self.readingFromSerialState = True
            self.animationFunc.event_source.start()
            self.consoleController.printToRightConsole("Starting serial reader")
            
        else:
            self.readingFromSerialState = False
            self.animationFunc.event_source.stop()
            self.consoleController.printToRightConsole("Pausing serial reader")

    def getData(self):
        if not self.rawLineData: return []
        self.data = []
        for index, value in enumerate(self.rawLineData[0]):
            graphLine = graphPage.graphLine(index, self.rawLineData[1][index],self.rawLineData[2][index], self.rawLineData[3][index] )  #id, name, axis, color
            self.data.append(graphLine)
        return self.data

    def goToSetupPage(self):
        self.parent.showPage("setup", self)
        if self.serialReader != None:
            self.serialReader.closeSerialConnection()

    def saveDataToFile(self, data):
        import os
        import json 

        filename = easygui.filesavebox(default=datetime.now().strftime("%Y-%m-%d_%H-%M")+".txt", filetypes=["*.txt"])

        if not filename: 
            self.consoleController.printToRightConsole("Couldn's save file. Filename not provided.")
            return

        with open(filename, mode="w+") as saveFile:
            
            linesStringified = []
            for line in data[0]:
                linesStringified.append(line.stringify())

            jsonString = json.dumps([linesStringified, data[1]])
            saveFile.write(jsonString)
            saveFile.close()

            self.consoleController.printToRightConsole("Successfully saved the data")
        if self.serialReader:
            self.serialReader.readingFromSerialState = False
        

    def setWindowSize(self, windowSize):
        if str.isdigit(windowSize):
            self.view.setWindowSize(float(windowSize))
            self.consoleController.printToRightConsole("Setting windowSize to %s" % windowSize)
