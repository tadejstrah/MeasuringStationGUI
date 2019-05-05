import tkinter as ttk
import setupPage as SP
from random import randint
from tkinter import N,S,E,W


import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
import threading
import time

class mainPage(ttk.Frame):

    def changeShouldReadState(self):
        self.shouldSerialRead
        self.shouldSerialRead = not self.shouldSerialRead
        
    def shouldSerialReadFunc(self):   #serialReader počekira tole funkcijo da začne/neha delat
        return self.shouldSerialRead


    def __init__(self, parent, controller, dataClass,serialReader):
        ttk.Frame.__init__(self,parent)

        self.windowSize = 10

        self.shouldSerialRead= False
        self._dataClass = dataClass
        self.serialReaderRef = serialReader
        self.controller = controller

        toolbarContainer = ttk.Frame(self)
        toolbarContainer.grid(sticky=W, row=2, column=0)

        self.checkboxes = []

        fig = plt.Figure()
        fig.subplots_adjust(left=0.05,right=0.96,bottom=0.05,top=0.96)


        ax1 = fig.add_subplot(111)
        ax2 = ax1.twinx()

        self.graphLines = []
        for x in self._dataClass:
            self.graphLines.append("")

        for x in range(len(self._dataClass)):
            if self._dataClass[x]._axis == "mA":
                self.graphLines[x], = ax1.plot(0,0)
            else:
                self.graphLines[x], = ax2.plot(0,0)
            self.graphLines[x].set_color(self._dataClass[x]._color)


       # ax1 = fig.add_subplot(111)
        #self.line1, = ax1.plot(0, 0)
        #   ax1.margins(0.5,tight=True)

        #ax2 = ax1.twinx()
        #self.line2, = ax2.plot(0,0)
        #self.line2.set_color("red")
        
        #self.nLine, = ax1.plot(0,0)

        plotCanvas = FigureCanvasTkAgg(fig, self)
        plotCanvas.get_tk_widget().grid(column=0, row=0, sticky=(N,S,E,W))

        toolbar = NavigationToolbar2Tk(plotCanvas, toolbarContainer)

        toolbar.lift()
        toolbar.update()

        
        self.ani = FuncAnimation(fig, self. run, interval=100,repeat=True)

        commandsFrame = ttk.Frame(self)
        commandsFrame.grid(column=1,row=0,sticky=(E,W,N))

        testButton = ttk.Button(commandsFrame, text="Back to setup page",command=lambda:self.goBackToSetupPage(controller))
        testButton.grid(column=1,row=1,pady=10) 

        self.playPauseLogo = ttk.PhotoImage(file="img\playpause2.png")
        self.playPauseLogo = self.playPauseLogo.subsample(2,2)
        startSerialButton = ttk.Button(commandsFrame,image=self.playPauseLogo, command=lambda:self.changeShouldReadState())
        startSerialButton.grid(column=1,row=2)
        
        windowSizeLabel = ttk.Label(commandsFrame, text="Plotting window size:")
        windowSizeLabel.grid(column=1,row=3,pady=(30,0))

        windowSizeEntry = ttk.Entry(commandsFrame)
        windowSizeEntry.insert(0, 30) #default value 
        windowSizeEntry.grid(column=1,row=4,pady=(5,5))

        setWindowSizeButton = ttk.Button(commandsFrame,text="Set window size",command=lambda:self.setWindowSize(windowSizeEntry))
        setWindowSizeButton.grid(column=1,row=5, pady=(5,20))

        for x in range(len(dataClass)):

            lineFrame = ttk.Frame(commandsFrame)
            lineFrame.grid(column=1, row=x+6)

            emptyLabel = ttk.Label(lineFrame,text="   ", background=dataClass[x]._color)
            emptyLabel.grid(row=0,column=0)

            var = ttk.BooleanVar(value=True)
            self.checkboxes.append(var)
            lineCheckbox = ttk.Checkbutton(lineFrame, text =dataClass[x]._name, var=var, command=self.callBackFunc)
            lineCheckbox.grid(row=0,column=1)

    def callBackFunc(self):
        for x in range(len(self.checkboxes)):
            self.graphLines[x].set_visible(self.checkboxes[x].get())
           # (self.checkboxes[x].get())
        #print("callback func")

    def setWindowSize(self,windowSizeEntry):
        winSize = windowSizeEntry.get()
        if winSize.isdigit():
            if self._dataClass[0].XData[-1] < int(winSize):
                self.controller.printToConsole("Window cannot be larger than the current amount of data\n", False)
            else:
                self.windowSize = int(winSize)
                self.controller.printToConsole("Setting window size to "+str(self.windowSize)+"\n",False)
        else:
            self.controller.printToConsole("Window size must be a positive integer, not"+str(winSize)+"\n",False)

        

    def goBackToSetupPage(self,controller):
        controller.showFrame(SP.setupPage)
        self.serialReaderRef.closeSerialConnection()



    def run(self,i):  #funkcija je klicana vsakih n miliskeund 
        try:
            if self._dataClass:
                #print(self._dataClass[1].XData)
                for x in range(len(self._dataClass)):
                    self.graphLines[x].set_data(self._dataClass[x].XData, self._dataClass[x].YData)

                windowSize = self.windowSize
                if self._dataClass[0].XData[-1] > windowSize:
                    if self.shouldSerialRead:
                        self.graphLines[1].axes.set_xlim(self._dataClass[0].XData[-1]-windowSize,self._dataClass[0].XData[-1]+self.windowSize/50)

                else:
                    self.graphLines[1].axes.relim()
                    self.graphLines[1].axes.autoscale_view()
                
                if len(self._dataClass) > 1:
                    for x in range(0,len(self.graphLines)-1):
                        self.graphLines[x+1].axes.relim()
                        self.graphLines[x+1].axes.autoscale_view()
                #self.line2.axes.relim()
                #self.line2.axes.autoscale_view()
            
        except: 
            print("animation func exception")