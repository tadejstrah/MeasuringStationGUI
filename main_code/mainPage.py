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


    def __init__(self, parent, controller, dataClass):
        ttk.Frame.__init__(self,parent)

        self.shouldSerialRead= False
        self._dataClass = dataClass

        #self._serialReaderRefference = serialReader
        
        toolbarContainer = ttk.Frame(self)
        toolbarContainer.grid(sticky=W, row=2, column=0)

        #row=3,column=0,sticky=(N,S,W,E)

        fig = plt.Figure()
        ax1 = fig.add_subplot(111)
        self.line1, = ax1.plot(0, 0)

        ax2 = ax1.twinx()
        self.line2, = ax2.plot(0,0)
        self.line2.set_color("red")
        #self.nLine, = ax1.plot(0,0)

        plotCanvas = FigureCanvasTkAgg(fig, self)
        plotCanvas.get_tk_widget().grid(column=0, row=0, sticky=(N,S,E,W))

        toolbar = NavigationToolbar2Tk(plotCanvas, toolbarContainer)

        toolbar.lift()
        toolbar.update()

        
        self.ani = FuncAnimation(fig, self. run, interval=100,repeat=True)

        commandsFrame = ttk.Frame(self)
        commandsFrame.grid(column=1,row=0,sticky=(E,W,N))

       # testLabel = ttk.Label(commandsFrame,text="test label on main page")
       # testLabel.grid(column=0,row=0)

        testButton = ttk.Button(commandsFrame, text="test button on main page",command=lambda:controller.showFrame(SP.setupPage))
        testButton.grid(column=1,row=1) 

        startSerialButton = ttk.Button(commandsFrame,text="start/stop serial", command=lambda:self.changeShouldReadState())
        startSerialButton.grid(column=1,row=2)
        
        


    def run(self,i):  #funkcija je klicana vsakih n miliskeund 
        if self._dataClass:
            self.line1.set_data(self._dataClass[1].XData, self._dataClass[1].YData)
            #self.line1.set_data(self._dataClass[2].XData, self._dataClass[2].YData)
            self.line2.set_data(self._dataClass[5].XData, self._dataClass[5].YData)
            #print(self._dataClass[0]._color)
            #print(self._dataClass[0].XData)

        
        self.line1.axes.relim()
        self.line1.axes.autoscale_view()
        self.line2.axes.relim()
        self.line2.axes.autoscale_view()
        
