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
        toolbarContainer.grid(sticky=W, row=10, column=0)

        #row=3,column=0,sticky=(N,S,W,E)

        fig = plt.Figure()
        ax1 = fig.add_subplot(111)
        self.hLine, = ax1.plot(0, 0)

        self.nLine, = ax1.plot(0,0)

        plotCanvas = FigureCanvasTkAgg(fig, self)
        plotCanvas.get_tk_widget().grid(column=0, row=0, sticky=(N,S,E,W))

        toolbar = NavigationToolbar2Tk(plotCanvas, toolbarContainer)
       # toolbar.grid()
        #toolbar.pack()
        print(toolbar)
        toolbar.lift()
        toolbar.update()

        
        self.ani = FuncAnimation(fig, self. run, interval=100,repeat=True)

        testLabel = ttk.Label(self,text="test label on main page")
        testLabel.grid()

        testButton = ttk.Button(self, text="test button on main page",command=lambda:controller.showFrame(SP.setupPage))
        testButton.grid() 

        startSerialButton = ttk.Button(self,text="start/stop serial", command=lambda:self.changeShouldReadState())
        startSerialButton.grid()
        
    def run(self,i):  #funkcija je klicana vsakih n miliskeund 
        #print("drawing to graph")
        #print(self._dataClass)
        if self._dataClass:
            #print(self._dataClass[5].XData)
            self.hLine.set_data(self._dataClass[3].XData, self._dataClass[3].YData)
            self.nLine.set_data(self._dataClass[2].XData, self._dataClass[2].YData)
            #print(self._dataClass[0]._color)
            #print(self._dataClass[0].XData)
        self.hLine.axes.relim()
        self.hLine.axes.autoscale_view()

