
import tkinter
import tkinter as ttk
import setupPage as SP

#import matplotlib
#import matplotlib.backends.tkagg as tkagg
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg#, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
#import matplotlib.animation as animation

class mainPage(ttk.Frame):
    '''
    xarr = []
    yarr = []
    fig = None
    ax1 = None
    line = None

    def animate(self,i):
        self.yarr.append(99)
        self.xarr.append(i)
        self.line.set_data(self.xarr,self.yarr)
        self.ax1.plot(self.xarr,self.yarr)
    '''
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self,parent)

        testLabel = ttk.Label(self,text="test label on main page")
        testLabel.grid()

        testButton = ttk.Button(self, text="test button on main page",command=lambda:controller.showFrame(SP.setupPage))
        testButton.grid() 
        ''' 
        self.xarr = []
        self.yarr = []

        style.use("ggplot")
        self. fig = plt.figure(figsize=(14,4.5), dpi=100)
        self.ax1 = self.fig.add_subplot(1,1,1)
        self.line = self.ax1.plot(self.xarr,self.yarr,"r",marker="o")


        plotcanvas = FigureCanvasTkAgg(self.fig,self)
        plotcanvas.get_tk_widget().grid(column=0,row=3)
        ani = animation.FuncAnimation(self.fig, self.animate,interval=1000)
        '''