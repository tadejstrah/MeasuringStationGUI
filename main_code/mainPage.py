
#from tkinter import *
import tkinter as ttk
import setupPage as SP
from random import randint

import matplotlib

import matplotlib.pyplot as plt
#import matplotlib.animation as animation
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation

import threading
import time
from queue import Queue


class GraphLine():
    def __init__(self):
        self.XData = [0]
        self.YData = [0]

#graphLines = [GraphLine()]

class mainPage(ttk.Frame):

    def __init__(self, parent, controller, dataClass):


        ttk.Frame.__init__(self,parent)

        self._dataClass = dataClass

        fig = plt.Figure()
        ax1 = fig.add_subplot(111)

        self.hLine, = ax1.plot(0, 0)

        plotCanvas = FigureCanvasTkAgg(fig, self)
        plotCanvas.get_tk_widget().grid(column=0, row=0)

        self.ani = FuncAnimation(fig, self. run, interval=500,repeat=True)

        testLabel = ttk.Label(self,text="test label on main page")
        testLabel.grid()

        testButton = ttk.Button(self, text="test button on main page",command=lambda:controller.showFrame(SP.setupPage))
        testButton.grid() 

    def run(self,i):
        self.hLine.set_data(self._dataClass.XData, self._dataClass.YData)
        print("setting data")
        self.hLine.axes.relim()
        self.hLine.axes.autoscale_view()

class SerialRead(threading.Thread):
    def __init__(self,dataClass):
        threading.Thread.__init__(self)

        self._dataClass = dataClass
    
    def run(self):
        while True:
            print("updating data")
            self._dataClass.XData.append(self._dataClass.XData[-1] + 1)
            self._dataClass.YData.append(randint(0,256))
            time.sleep(0.1)