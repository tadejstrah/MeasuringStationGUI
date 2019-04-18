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
from queue import Queue

class mainPage(ttk.Frame):

    def changeShouldReadState(self):
        self.shouldSerialRead
        self.shouldSerialRead = not self.shouldSerialRead
        #self._serialReaderRefference.lineArray = []

    def shouldSerialReadFunc(self):   #serialReader počekira tole funkcijo da začne/neha delat
        return self.shouldSerialRead


    def __init__(self, parent, controller, dataClass,serialReader):
        ttk.Frame.__init__(self,parent)

        self.windowSize = 10

        self.shouldSerialRead= False
        self._dataClass = dataClass
        self.serialReaderRef = serialReader
        self.controller = controller
        #self.ser = serReff
        #self._serialReaderRefference = serialReader
        
        toolbarContainer = ttk.Frame(self)
        toolbarContainer.grid(sticky=W, row=2, column=0)

        #row=3,column=0,sticky=(N,S,W,E)

        
        fig = plt.Figure()
        #ax = fig.add_axes([0.03,0.05,0.96,0.96])
        fig.subplots_adjust(left=0.05,right=0.96,bottom=0.05,top=0.96)

        ax1 = fig.add_subplot(111)
        self.line1, = ax1.plot(0, 0)
        #   ax1.margins(0.5,tight=True)

        ax2 = ax1.twinx()
        self.line2, = ax2.plot(0,0)
        self.line2.set_color("red")
        
        #self.nLine, = ax1.plot(0,0)

        plotCanvas = FigureCanvasTkAgg(fig, self)
        plotCanvas.get_tk_widget().grid(column=0, row=0, sticky=(N,S,E,W))

        toolbar = NavigationToolbar2Tk(plotCanvas, toolbarContainer)

        toolbar.lift()
        toolbar.update()

        
        self.ani = FuncAnimation(fig, self. run, interval=70,repeat=True)

        commandsFrame = ttk.Frame(self)
        commandsFrame.grid(column=1,row=0,sticky=(E,W,N))

       # testLabel = ttk.Label(commandsFrame,text="test label on main page")
       # testLabel.grid(column=0,row=0)

        testButton = ttk.Button(commandsFrame, text="test button on main page",command=lambda:self.goBackToSetupPage(controller))
        testButton.grid(column=1,row=1,pady=10) 

        startSerialButton = ttk.Button(commandsFrame,text="start/stop serial", command=lambda:self.changeShouldReadState())
        startSerialButton.grid(column=1,row=2)
        
        windowSizeEntry = ttk.Entry(commandsFrame)
        windowSizeEntry.insert(0, 30) #default value je 50
        windowSizeEntry.grid(column=1,row=3,pady=(30,5))

        setWindowSizeButton = ttk.Button(commandsFrame,text="Set window size",command=lambda:self.setWindowSize(windowSizeEntry))
        setWindowSizeButton.grid(column=1,row=4)


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
        if self._dataClass:
            if len(self._dataClass[1].XData) == len(self._dataClass[1].YData):
                self.line1.set_data(self._dataClass[1].XData, self._dataClass[1].YData)
            #self.line1.set_data(self._dataClass[2].XData, self._dataClass[2].YData)
            if len(self._dataClass[5].XData) == len(self._dataClass[5].YData):
                self.line2.set_data(self._dataClass[5].XData, self._dataClass[5].YData)
            #print(self._dataClass[0]._color)
            #print(self._dataClass[0].XData)

            #print(self.windowSize)
            windowSize = self.windowSize
            
            #lenOfXData = len(self._dataClass[1].XData)
            #if lenOfXData > windowSize:
            if self._dataClass[1].XData[-1] > windowSize:
                if self.shouldSerialRead:
                    #xmin, xmax = self.line1.axes.get_xlim()
                    self.line1.axes.set_xlim(self._dataClass[1].XData[-1]-windowSize,self._dataClass[1].XData[-1]+self.windowSize/50)
                    #self.line1.axes.set_xlim((lenOfXData-windowSize)/40,lenOfXData/40)
                    #self.line1.axes.relim()
                    #self.line1.axes.autoscale_view()
                    #self.line1.axes.autoscale(axis={"y"})

            else:
            #self.line1.axes.set_xlim(10,100)
                self.line1.axes.relim()
                self.line1.axes.autoscale_view()
            self.line2.axes.relim()
            self.line2.axes.autoscale_view()
        
