import tkinter
import tkinter as ttk
from tkinter import N,S,W,E
import mainPage as MP
from tkinter import IntVar
from tkinter.colorchooser import *
import GraphLine 
import csv
from tkinter.ttk import *
 
import dataManager

class setupPage(ttk.Frame):

    def __init__(self,parent,controller,dataArrRefference):
        ttk.Frame.__init__(self,parent)

        self.defaultNrOfLines = 5

        self.labels=[] #array of label widgets

        self.dataManager = dataManager.dataManager(dataArrRefference)

        #configuration of container frame - takes care of rescaling,...
        containerFrame = Frame(self)
        containerFrame.grid(column=0,row=0,sticky=(N,S,W,E))
        containerFrame.rowconfigure(0,weight=1)
        containerFrame.rowconfigure(1,weight=1)
        containerFrame.rowconfigure(2,weight=1)
        containerFrame.columnconfigure(0,weight=1)

        self._dataArrRefference = dataArrRefference #shared data object/array

        self.colorComboBoxes = [] #array of color-selection comboboxes
        self.axisComboBoxes = [] #array of axis-selection comboboxes
        self.nameInputs = []   #array of text entries for name selection

        dropDown_frame = Frame(containerFrame) #frame, that houses Combobox for nr-of-lines selection
        dropDown_frame.grid(column=0,row=0,sticky=(N,S,W,E))

        self.graphLinesSelector_frame = Frame(containerFrame) #frame that houses all of the line setup widgets
        self.graphLinesSelector_frame.grid(column=0,row=1,sticky=(N,S,W,E))

        openFileButton_frame = Frame(containerFrame)
        openFileButton_frame.grid(column=0, row=2, sticky=(N,S,W,E))

        continueButton_frame = Frame(containerFrame) #frame that holds button for continueuing to next (main) page
        continueButton_frame.grid(column=0,row=3,sticky=(S,W,E))

        self.numberOfParams = 1 #number of lines; this value gets changed later in the code to either defaultNrOfLines or nr. selected by te user

        options = [i for i in (range(1,10))] #list of possible nr. of lines

        dropDownMenu = Combobox(dropDown_frame,values=options,state="readonly") #combobox for selecting the nr of lines
        dropDownMenu.set(self.defaultNrOfLines) #setting default value
        dropDownMenu.bind('<<ComboboxSelected>>', self.on_dropDownMenu_select) #binding 
        dropDownMenu.grid()

        openFileButton = ttk.Button(openFileButton_frame, text="Open File", command=lambda: self.setDataFromOpenedFile(controller))
        openFileButton.grid(padx=10,pady=10)

        goToNextPageButton = ttk.Button(continueButton_frame, text="Setup complete, continue to the main page.",command=lambda:self.goToMainPageButtonAction(controller))
        goToNextPageButton.grid(padx=10,pady=10)


    def setDataFromOpenedFile(self, controller):
        controller.data = self.dataManager.openFile()
        #print(controller.data)
        #print(self.dataArrRefference)
        if not MP.mainPage in controller.frames.keys():
                controller.initMainPage()
        controller.showFrame(MP.mainPage)
        controller.serialReader.openSerial()
        #print(self.dataArrRefference[0].XData)


    def goToMainPageButtonAction(self,controller):
        if controller.data:
            for i in controller.serialReader._dataClass:
                i.XData = []
                i.YData = []
    
        if not controller.data:

            for i in range(len(self.labels)):
                graphLine = GraphLine.GraphLine(self.colorComboBoxes[i].get(),self.axisComboBoxes[i].get(),self.nameInputs[i].get())
                self._dataArrRefference.append(graphLine)
            if not MP.mainPage in controller.frames.keys():
                controller.initMainPage()

            
        with open("settingsCache.txt", mode="w", newline="\n") as cacheFile:
            cacheFile.truncate()
            csv_writer = csv.writer(cacheFile, delimiter=";") 
            for line in self._dataArrRefference:
                #print(line._name, line._axis, line._color)
                csv_writer.writerow([line._name, line._axis, line._color])
            cacheFile.close()

        controller.showFrame(MP.mainPage)
        controller.serialReader.openSerial()



    #ko user na dropdownu izbere vrednost se zgenerira UI (usi labeli, doprdowni...)
    def on_dropDownMenu_select(self,event=None):
        self.labels = []
        if not event:
            #proba prebrat cache settinge ob startupu (torej če ni event)
            try:
                with open("settingsCache.txt", mode="r") as cacheFile:
                    csv_reader = csv.reader(cacheFile, delimiter = ";")
                    counter = 0
                    for row in csv_reader:
                    
                        label = Label(self.graphLinesSelector_frame, text=str(counter))
                        label.grid(row=counter, column=0, padx=10, pady=0)
                        self.labels.append(label)

                        nameInput = ttk.Entry(self.graphLinesSelector_frame)
                        nameInput.insert(0,row[0])
                        nameInput.grid(row=counter, column=1)
                        self.nameInputs.append(nameInput)

                        axisCombobox = Combobox(self.graphLinesSelector_frame, values=["A","°","V"], state="readonly")
                        axisCombobox.set(row[1])
                        axisCombobox.grid(row=counter, column=2)
                        self.axisComboBoxes.append(axisCombobox)
                        
                        self.colorValues = ["red","blue","gold","green","black","purple","pink","yellow","brown"]
                        colorCombobox = Combobox(self.graphLinesSelector_frame,values=self.colorValues,state="readonly")
                        colorCombobox.set(row[2])
                        colorCombobox.bind('<<ComboboxSelected>>', self.on_colorMenuDropdown_select)
                        colorCombobox.grid(row=counter,column=3)
                        self.colorComboBoxes.append(colorCombobox)

                        counter += 1
            except Exception as e:
                print(e)
                print("neki druzga")
        #če je event (torej ne startup) se zgodi sledeče
        else:
            if event:
                self.numberOfParams = int(event.widget.get())
            else:
                self.numberOfParams = self.defaultNrOfLines
            for i in range(self.numberOfParams):
                self.labels.append(Label())
                self.colorComboBoxes.append(Combobox())
                self.axisComboBoxes.append(Combobox())
                self.nameInputs.append(ttk.Entry())

            for child in self.graphLinesSelector_frame.winfo_children():
                child.destroy()
            for i in range(self.numberOfParams):
                self.labels[i] = Label(self.graphLinesSelector_frame,text=(str(i+1)))
                self.labels[i].grid(row=i,column=0,pady=3,padx=10)

                self.nameInputs[i] = ttk.Entry(self.graphLinesSelector_frame)
                self.nameInputs[i].insert(0,"Label  " +str(i+1))
                self.nameInputs[i].grid(row=i,column=1)

                self.axisComboBoxes[i] = Combobox(self.graphLinesSelector_frame,values=["A","°","V"],state="readonly")
                if i == 4:
                    self.axisComboBoxes[i].set("°")
                else:
                    self.axisComboBoxes[i].set("mA")
                self.axisComboBoxes[i].grid(row=i,column=2,padx=3)

                self.colorValues = ["red","blue","gold","green","black","purple","pink","yellow","brown"]
                self.colorComboBoxes[i] = Combobox(self.graphLinesSelector_frame,values=self.colorValues,state="readonly")
                self.colorComboBoxes[i].set(self.colorValues[i])
                self.colorComboBoxes[i].bind('<<ComboboxSelected>>', self.on_colorMenuDropdown_select)
                self.colorComboBoxes[i].grid(row=i,column=3)


    #ko user selecta barvo se pobarva label - TODO implementaj da se pobarva tudi ko naloži iz cacha
    def on_colorMenuDropdown_select(self,event):
        if event:
            self.labels[int(event.widget.grid_info()["row"])].configure(background=event.widget.get()) #iz pozicije comboboxa na gridu najde indeks labela v arrayu in mu accordingly changa barvo
        
 