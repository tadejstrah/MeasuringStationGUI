
import tkinter
import tkinter as ttk
from tkinter import N,S,W,E
import mainPage as MP
from tkinter import IntVar
#from tkinter import Combobox
from tkinter.colorchooser import *

#from tkinter import *
from tkinter.ttk import *

class setupPage(ttk.Frame):


    def __init__(self,parent,controller,dataArrRefference):
        ttk.Frame.__init__(self,parent)

        self.labels=[]
        containerFrame = Frame(self)
        containerFrame.grid(column=0,row=0,sticky=(N,S,W,E))
        containerFrame.rowconfigure(0,weight=1)
        containerFrame.rowconfigure(1,weight=1)
        containerFrame.rowconfigure(2,weight=1)
        containerFrame.columnconfigure(0,weight=1)

        self._dataArrRefference = dataArrRefference


        dropDown_frame = Frame(containerFrame)
        dropDown_frame.grid(column=0,row=0,sticky=(N,S,W,E))

        self.graphLinesSelector_frame = Frame(containerFrame)
        self.graphLinesSelector_frame.grid(column=0,row=1,sticky=(N,S,W,E))

        continueButton_frame = Frame(containerFrame)
        continueButton_frame.grid(column=0,row=2,sticky=(S,W,E))

        self.numberOfParams = 1

        options = [1,2,3,4,5,6,7,8,9]

        dropDownMenu = Combobox(dropDown_frame,values=options)
        dropDownMenu.set(6)
        dropDownMenu.bind('<<ComboboxSelected>>', self.on_dropDownMenu_select)
        dropDownMenu.grid()




        label = ttk.Label(continueButton_frame,text="test label on setup page",background="red")
        label.grid()
        #label.grid(column=0,row=0,sticky=(S,E,W,N))
        label2 = ttk.Label(continueButton_frame,text="lbael 2",background="blue")
        label2.grid()

        testButton = ttk.Button(continueButton_frame, text="gotomainpage",command=lambda:controller.showFrame(MP.mainPage))
        testButton.grid()



    def on_dropDownMenu_select(self,event=None):
        
        self.numberOfParams = int(event.widget.get())
        for i in range(self.numberOfParams):
            self.labels.append(Label())

        for child in self.graphLinesSelector_frame.winfo_children():
            child.destroy()
        for i in range(self.numberOfParams):
            self.labels[i] = Label(self.graphLinesSelector_frame,text=("Label" + str(i+1)))
            self.labels[i].grid(row=i,column=0)

            AxisDropDown = Combobox(self.graphLinesSelector_frame,values=["mA","mW"])
            AxisDropDown.set("mA")
            AxisDropDown.grid(row=i,column=1)

            colorDropDown = Combobox(self.graphLinesSelector_frame,values=["red","blue","gold","green","black","purple"])
            colorDropDown.set("black")
            colorDropDown.bind('<<ComboboxSelected>>', self.on_colorMenuDropdown_select)
            colorDropDown.grid(row=i,column=2)

    def on_colorMenuDropdown_select(self,event):
        print(event.widget.grid_info()["row"])
        self.labels[int(event.widget.grid_info()["row"])].configure(background=event.widget.get())
        print(event.widget.get())

        
 
