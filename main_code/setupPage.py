import tkinter
import tkinter as ttk
from tkinter import N,S,W,E
import mainPage as MP
from tkinter import IntVar
#from tkinter import Combobox
from tkinter.colorchooser import *
import GraphLine

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

        self.colorComboBoxes = []
        self.axisComboBoxes = []

        dropDown_frame = Frame(containerFrame)
        dropDown_frame.grid(column=0,row=0,sticky=(N,S,W,E))

        self.graphLinesSelector_frame = Frame(containerFrame)
        self.graphLinesSelector_frame.grid(column=0,row=1,sticky=(N,S,W,E))

        continueButton_frame = Frame(containerFrame)
        continueButton_frame.grid(column=0,row=2,sticky=(S,W,E))

        self.numberOfParams = 1

        options = [1,2,3,4,5,6,7,8,9]

        dropDownMenu = Combobox(dropDown_frame,values=options,state="readonly")
        dropDownMenu.set(6)
        dropDownMenu.bind('<<ComboboxSelected>>', self.on_dropDownMenu_select)
        dropDownMenu.grid()


        label = ttk.Label(continueButton_frame,text="test label on setup page",background="red")
        label.grid()
        #label.grid(column=0,row=0,sticky=(S,E,W,N))
        label2 = ttk.Label(continueButton_frame,text="lbael 2",background="blue")
        label2.grid()

        testButton = ttk.Button(continueButton_frame, text="gotomainpage",command=lambda:self.goToMainPageButtonAction(controller))
        testButton.grid()

    def goToMainPageButtonAction(self,controller):
        for i in range(len(self.labels)):
            graphLine = GraphLine.GraphLine(self.colorComboBoxes[i].get(),self.axisComboBoxes[i].get())
            self._dataArrRefference.append(graphLine)

        if not MP.mainPage in controller.frames.keys():
            controller.initMainPage()
        controller.showFrame(MP.mainPage)




    def on_dropDownMenu_select(self,event=None):
        print(event)
        if event:
            self.numberOfParams = int(event.widget.get())
        else:
            self.numberOfParams = 6
        for i in range(self.numberOfParams):
            self.labels.append(Label())
            self.colorComboBoxes.append(Combobox())
            self.axisComboBoxes.append(Combobox())

        for child in self.graphLinesSelector_frame.winfo_children():
            child.destroy()
        for i in range(self.numberOfParams):
            self.labels[i] = Label(self.graphLinesSelector_frame,text=("Label" + str(i+1)))
            self.labels[i].grid(row=i,column=0)

            self.axisComboBoxes[i] = Combobox(self.graphLinesSelector_frame,values=["mA","°"],state="readonly")
            self.axisComboBoxes[i].set("mA")
            self.axisComboBoxes[i].grid(row=i,column=1)

            self.colorComboBoxes[i] = Combobox(self.graphLinesSelector_frame,values=["red","blue","gold","green","black","purple"],state="readonly")
            self.colorComboBoxes[i].set("black")
            self.colorComboBoxes[i].bind('<<ComboboxSelected>>', self.on_colorMenuDropdown_select)
            self.colorComboBoxes[i].grid(row=i,column=2)

    def on_colorMenuDropdown_select(self,event):
        if event:
            self.labels[int(event.widget.grid_info()["row"])].configure(background=event.widget.get()) #iz pozicije comboboxa na gridu najde indeks labela v arrayu in mu accordingly changa barvo
        
 