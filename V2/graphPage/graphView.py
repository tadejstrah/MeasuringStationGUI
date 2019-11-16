import tkinter as tk
from tkinter import N,S,W,E

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.animation import FuncAnimation
#matplotlib.use('TkAgg')


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

        fig = plt.Figure()
        fig.subplots_adjust(left=0.05,right=0.96,bottom=0.05,top=0.96)
        self.ax1 = fig.add_subplot(111)

        plotCanvas = FigureCanvasTkAgg(fig, self.container)
        plotCanvas.get_tk_widget().grid(column=0, row=1, sticky=(N,S,E,W))

        toolbar = NavigationToolbar2Tk(plotCanvas, self.toolbarFrame)
        toolbar.lift()
        toolbar.update()


        #Button = tk.Button(self.container, text="neki neki na graph viewvu", command=lambda:self.parent.showPage("setup", self))
        #Button.grid(padx=10,pady=10, row=0, column=0) 


        backToSetupPageButton = tk.Button(self.commandsFrame, text="Back to setup page", command=None)
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

        saveDataButton = tk.Button(commandsFrame, text="Save data to csv",command=None)
        saveDataButton.grid(column=1,row=15,pady=10)

    def draw(self):
         

        data = self.controller.getData()
        #print(data)

        self.ax1.plot([1,2,3,4,5],[4,5,2,5,3]) #test plot
        #self.ax1.autoscale(enable=True) 

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