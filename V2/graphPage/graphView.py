import tkinter as tk
from tkinter import N,S,W,E

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.animation import FuncAnimation
#matplotlib.use('TkAgg')
import random

from itertools import cycle

import defaults

class graphView(tk.Frame):
    def __init__(self, parent, frame):
        tk.Frame.__init__(self,parent)

        self.parent = parent
        self.controller = None
        self.consoleController = parent.getControllerRefferenceOf("console")

        self.data = None
        self.time = []

        self.container = tk.Frame(self)
        self.container.grid(row=0, column=0, sticky = (N, S ,W ,E))
        self.container.rowconfigure(1, weight=1)
        self.container.columnconfigure(0, weight=1)
        #self.container.columnconfigure(1, weight=1)


        self.commandsFrame = tk.Frame(self.container)
        self.commandsFrame.grid(column=1, row=1, sticky=(N,W,E,S))

        self.toolbarFrame = tk.Frame(self.container)
        self.toolbarFrame.grid(row=2, column=0, sticky=W)

        self.toolbar = None

        self.windowSize = 50 #default


    def draw(self):
        #print("drawing on graphView")
        self.data = self.controller.getData()

        self.fig = plt.Figure()
        self.fig.subplots_adjust(left=0.05,right=0.95,bottom=0.05,top=0.96)
        self.ax1 = self.fig.add_subplot(111)

        self.plotCanvas = FigureCanvasTkAgg(self.fig, self.container)
        self.plotCanvas.get_tk_widget().grid(column=0, row=1, sticky=(N,S,E,W))

        if self.toolbar:
            self.toolbar.destroy()
        self.toolbar = NavigationToolbar2Tk(self.plotCanvas, self.toolbarFrame)
        self.toolbar.lift()
        self.toolbar.update()


        for child in self.commandsFrame.winfo_children():
            child.destroy()        

        backToSetupPageButton = tk.Button(self.commandsFrame, text="Back to setup page", command=self.controller.goToSetupPage)
        backToSetupPageButton.grid(column=1, row=1, pady=10)

        self.playPauseLogo = tk.PhotoImage(file="img\playpause2.png")
        self.playPauseLogo = self.playPauseLogo.subsample(2,2)
        startSerialButton = tk.Button(self.commandsFrame,image=self.playPauseLogo, command=self.controller.changeReadingFromSerialState)
        startSerialButton.grid(column=1,row=2)

        windowSizeLabel = tk.Label(self.commandsFrame, text="Plotting window size:")
        windowSizeLabel.grid(column=1,row=3,pady=(30,0))

        windowSizeEntry = tk.Entry(self.commandsFrame)
        windowSizeEntry.insert(0, 30) #default value 
        windowSizeEntry.grid(column=1,row=4,pady=(5,5))

        setWindowSizeButton = tk.Button(self.commandsFrame,text="Set window size",command=lambda:self.controller.setWindowSize(windowSizeEntry.get()))
        setWindowSizeButton.grid(column=1,row=5, pady=(5,20))

        saveDataButton = tk.Button(self.commandsFrame, text="Save data to .json file",command=lambda:self.controller.saveDataToFile([self.data, self.time]))
        saveDataButton.grid(column=1,row=40,pady=10)



        self.axes = {}

        allAxesTypes = list(i.axis for i in self.data)

        #nardi dict različnih skal
        self.axes[allAxesTypes[0]] = self.ax1
        for axis in allAxesTypes[1:]:
            if axis not in self.axes.keys():
                self.axes[axis] = self.ax1.twinx()

        axesTypesHashMap = list(set(i.axis for i in self.data))
        
        extraYs = len(list(self.axes.keys())[2:]) #zračuna odmik dodatnih oznak skal
        if extraYs>0:
            temp = 0.5
            if extraYs<=2:
                temp = 0.9
            elif extraYs<=4:
                temp = 0.85
            if extraYs>5:
                print("your being redicoulous")
            self.fig.subplots_adjust(right=temp)
            right_additive = (0.98-temp)/float(extraYs)   

        #dodajanje ekstra oznak skal
        for i, ax in enumerate(list(self.axes.keys())[2:]):
            self.axes[ax].spines['right'].set_position(('axes', 1.+right_additive*(i+1)))
            self.axes[ax].set_frame_on(True)
            self.axes[ax].patch.set_visible(False)
            self.axes[ax].yaxis.set_major_formatter(matplotlib.ticker.OldScalarFormatter())

        colors = cycle(defaults.predefinedColors)
        line_styles = cycle(defaults.lineStyles)
        
        for index, axisType in enumerate(allAxesTypes): #nardi line objekte in jih appenda ljubemu data arrayu
            ls=next(line_styles)
            label = axisType
            self.data[index].line = self.axes[axisType].plot([0],[0], linestyle=ls, label=label, color=self.data[index].color)[0]

        axesNames = {} #nardi labele za oznake axisov - unit + imena line-ov
        for line in self.data:
            if line.axis not in axesNames.keys():
                axesNames[line.axis] = ("Unit: " + line.axis + "     Lines: " + line.name + " , ")
            else:
                axesNames[line.axis] += line.name + ", "
            axesNames[line.axis] = axesNames[line.axis][:-2] #remova zadnjo vejico in presledek k sta odveč

        for index, axis in enumerate(self.axes.values()): #setta labele oznak axisov in relim-a
            axis.relim()
            axis.autoscale_view()
            axis.set_ylabel(axesNames[list(axesNames.keys())[index]])

        labels = [line.name for line in self.data]
        lines = [line.line for line in self.data]
        self.axes[list(self.axes.keys())[0]].legend(lines,labels, loc=1) #setta legendo


        self.checkboxes = []

        for index, line in enumerate(self.data): #create checkboxes to toggle line visibiltiy
            lineFrame = tk.Frame(self.commandsFrame)
            lineFrame.grid(column=1, row=index+6)

            emptyLabel = tk.Label(lineFrame,text="   ", background=line.color)
            emptyLabel.grid(row=0,column=0)

            var = tk.BooleanVar(value=True)
            self.checkboxes.append(var)
            lineCheckbox = tk.Checkbutton(lineFrame, text =line.name, var=var, command=self.toggleLineVisibility)
            lineCheckbox.grid(row=0,column=1)

    def toggleLineVisibility(self):
        for index, checkbox in enumerate(self.checkboxes):
            self.data[index].line.set_visible(self.checkboxes[index].get()) #set line's visibilityb
            self.plotCanvas.draw() #updates the graph

    def setWindowSize(self, windowSize):
        self.windowSize = windowSize
    
    def getLastTimeValue(self):
        return self.time[-1]


    def updateGraph(self, newData):
        #print("updating graph")
        #print("newData[0]:", str(newData[0]))
        #print("newData[1]:", str(newData[1]))

        if len(newData)==0: return
        newTime = newData[1]
        newData = newData[0]

        for t in newTime:
            try: floatOfTime = float(t)
            except: floatOfTime = self.time[-1] #če conversion faila da default time[-1]
            self.time.append(floatOfTime)
        #print(newData)

        for index, oneLineOfNewData in enumerate(newData):
            self.consoleController.printToLeftConsole("Time: \t"+ str(self.time[-1]) + "\t Values: "+ "".join("\t"+i for i in oneLineOfNewData) + "\t")
            for index2,paramValue in enumerate(oneLineOfNewData):  #param value je recimo vrednost napetosti v eni od prejetih vrstic v newData
                if index2 > len(self.data)-1: #če je index out of range, menaing da na grafu ni tolko črt kot jih dobi program iz seriala
                    break
                try: floatOfParamValue = float(paramValue)
                except: floatOfParamValue = 0.0 #default value
                self.data[index2].YData.append(floatOfParamValue)

        for line in self.data:
            line.line.set_data(self.time[0:len(line.YData)], line.YData)
            

        for index, axis in enumerate(self.axes.values()): #setta labele oznak axisov in relim-a
            if self.windowSize < self.time[-1]:
                axis.set_xlim(self.time[-1]-self.windowSize, self.time[-1])
            axis.relim()
            axis.autoscale_view()
        
