import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import threading
import random
import time

import tkinter as ttk

from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure



class MyDataClass():

    def __init__(self):

        self.XData = [0]
        self.YData = [0]


class MyPlotClass(ttk.Frame):

    def __init__(self, dataClass,parent):
        ttk.Frame.__init__(self,parent)
        self._dataClass = dataClass

        fig = plt.Figure()
        ax1 = fig.add_subplot(111)

        self.hLine, = ax1.plot(0, 0)


        plotcanvas = FigureCanvasTkAgg(fig, parent)
        plotcanvas.get_tk_widget().grid(column=0,row=0)

        self.ani = FuncAnimation(fig, self.run, interval = 1000, repeat=True)


    def run(self, i):  
        print("plotting data")
        self.hLine.set_data(self._dataClass.XData, self._dataClass.YData)
        self.hLine.axes.relim()
        self.hLine.axes.autoscale_view()


class MyDataFetchClass(threading.Thread):

    def __init__(self, dataClass):

        threading.Thread.__init__(self)

        self._dataClass = dataClass
        self._period = 0.25
        self._nextCall = time.time()


    def run(self):

        while True:
            print("updating data")
            # add data to data class
            self._dataClass.XData.append(self._dataClass.XData[-1] + 1)
            self._dataClass.YData.append(random.randint(0, 256))
            # sleep until next execution
           # self._nextCall = self._nextCall + self._period
            #time.sleep(self._nextCall - time.time())
            time.sleep(0.1)


root = ttk.Tk()


data = MyDataClass()
plotter = MyPlotClass(data,root)
fetcher = MyDataFetchClass(data)

fetcher.daemon = True
fetcher.start()
#plt.show()


root.mainloop()