import tkinter as ttk
import setupPage as SP
from random import randint
from tkinter import N,S,E,W


import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation

import threading
import time
from queue import Queue




#graphLines = [GraphLine()]

class mainPage(ttk.Frame):



    def changeShouldReadState(self):
        self.shouldSerialRead
        self.shouldSerialRead = not self.shouldSerialRead
        print("changing state")

    def shouldSerialReadFunc(self):
        return self.shouldSerialRead


    def __init__(self, parent, controller, dataClass):

        self.shouldSerialRead= True

        ttk.Frame.__init__(self,parent)

        self._dataClass = dataClass

        fig = plt.Figure()
        ax1 = fig.add_subplot(111)

        self.hLine, = ax1.plot(0, 0)

        plotCanvas = FigureCanvasTkAgg(fig, self)
        plotCanvas.get_tk_widget().grid(column=0, row=0, sticky=(N,S,E,W))

        self.ani = FuncAnimation(fig, self. run, interval=500,repeat=True)

        testLabel = ttk.Label(self,text="test label on main page")
        testLabel.grid()

        testButton = ttk.Button(self, text="test button on main page",command=lambda:controller.showFrame(SP.setupPage))
        testButton.grid() 

        startSerialButton = ttk.Button(self,text="start/stop serial", command=lambda:self.changeShouldReadState())
        startSerialButton.grid()

    def run(self,i):
        self.hLine.set_data(self._dataClass.XData, self._dataClass.YData)
        #print("setting data")
       # print(shouldSerialRead)
        self.hLine.axes.relim()
        self.hLine.axes.autoscale_view()

