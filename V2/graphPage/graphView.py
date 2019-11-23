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


        

        self.container = tk.Frame(self)
        self.container.grid(row=0, column=0, sticky = (N, S ,W ,E))
        self.container.rowconfigure(1, weight=1)
        self.container.columnconfigure(0, weight=1)
        #self.container.columnconfigure(1, weight=1)


        self.commandsFrame = tk.Frame(self.container)
        self.commandsFrame.grid(column=1, row=1, sticky=(N,W,E,S))

        self.toolbarFrame = tk.Frame(self.container)
        self.toolbarFrame.grid(row=2, column=0, sticky=W)

        self.fig = plt.Figure()
        self.fig.subplots_adjust(left=0.05,right=0.95,bottom=0.05,top=0.96)
        self.ax1 = self.fig.add_subplot(111)

        plotCanvas = FigureCanvasTkAgg(self.fig, self.container)
        plotCanvas.get_tk_widget().grid(column=0, row=1, sticky=(N,S,E,W))

        toolbar = NavigationToolbar2Tk(plotCanvas, self.toolbarFrame)
        toolbar.lift()
        toolbar.update()




    def draw(self):
         
        data = self.controller.getData()

        #print(data)

        for child in self.commandsFrame.winfo_children():
            child.destroy()        

        backToSetupPageButton = tk.Button(self.commandsFrame, text="Back to setup page", command=self.controller.goToSetupPage)
        backToSetupPageButton.grid(column=1, row=1, pady=10)

        self.playPauseLogo = tk.PhotoImage(file="img\playpause2.png")
        self.playPauseLogo = self.playPauseLogo.subsample(2,2)
        startSerialButton = tk.Button(self.commandsFrame,image=self.playPauseLogo, command=None)
        startSerialButton.grid(column=1,row=2)

        windowSizeLabel = tk.Label(self.commandsFrame, text="Plotting window size:")
        windowSizeLabel.grid(column=1,row=3,pady=(30,0))

        windowSizeEntry = tk.Entry(self.commandsFrame)
        windowSizeEntry.insert(0, 30) #default value 
        windowSizeEntry.grid(column=1,row=4,pady=(5,5))

        setWindowSizeButton = tk.Button(self.commandsFrame,text="Set window size",command=None)
        setWindowSizeButton.grid(column=1,row=5, pady=(5,20))

        saveDataButton = tk.Button(self.commandsFrame, text="Save data to csv",command=None)
        saveDataButton.grid(column=1,row=40,pady=10)



        axes = {}

        allAxesTypes = list(i.axis for i in data)

        #nardi dict različnih skal
        axes[allAxesTypes[0]] = self.ax1
        for axis in allAxesTypes[1:]:
            if axis not in axes.keys():
                axes[axis] = self.ax1.twinx()


        axesTypesHashMap = list(set(i.axis for i in data))
        
        extraYs = len(list(axes.keys())[2:]) #zračuna odmik dodatnih oznak skal
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
        for i, ax in enumerate(list(axes.keys())[2:]):
            #print("more than two axes, adding aditional scale")
            axes[ax].spines['right'].set_position(('axes', 1.+right_additive*(i+1)))
            axes[ax].set_frame_on(True)
            axes[ax].patch.set_visible(False)
            axes[ax].yaxis.set_major_formatter(matplotlib.ticker.OldScalarFormatter())


        colors = cycle(defaults.predefinedColors)
        line_styles = cycle(defaults.lineStyles)
        
        for index, axisType in enumerate(allAxesTypes): #nardi line objekte
            ls=next(line_styles)
            label = axisType
            data[index].line = axes[axisType].plot([0],[0], linestyle=ls, label=label, color=data[index].color)[0]

        for i in data: #dummy data
            i.line.set_data([i for i in range(5)],[random.randint(0,i*5+2) for i in range(5)])


        axesNames = {} #nardi labele za oznake axisov
        for line in data:
            if line.axis not in axesNames.keys():
                axesNames[line.axis] = (line.name + ", ")
            else:
                axesNames[line.axis] += line.name + " "

        for index, axis in enumerate(axes.values()): #setta labele oznak axisov in relim-a
            axis.relim()
            axis.autoscale_view()
            axis.set_ylabel(axesNames[list(axesNames.keys())[index]])

        labels = [line.name for line in data]
        lines = [line.line for line in data]
        axes[list(axes.keys())[0]].legend(lines,labels, loc=0) #setta legendo


        self.checkboxes = []

        for index, line in enumerate(data):
            lineFrame = tk.Frame(self.commandsFrame)
            lineFrame.grid(column=1, row=index+6)

            emptyLabel = tk.Label(lineFrame,text="   ", background=line.color)
            emptyLabel.grid(row=0,column=0)

            var = tk.BooleanVar(value=True)
            self.checkboxes.append(var)
            lineCheckbox = tk.Checkbutton(lineFrame, text =line.name, var=var, command=self.toggleLineVisibility)
            lineCheckbox.grid(row=0,column=1)

    def toggleLineVisibility(self):
        pass