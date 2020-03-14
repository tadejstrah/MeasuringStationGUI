import tkinter as tk
from tkinter import N,S,W,E, RAISED
from tkinter.ttk import Combobox
import defaults

from tkinter.colorchooser import *


class setupView(tk.Frame):
    def __init__(self, parent, frame):
        tk.Frame.__init__(self,parent)

        self.parent = parent
        self.controller = None

        self.linesSettings = []

        self.masterContainer = tk.Frame(self, bg= "dark gray")
        self.masterContainer.grid(row=0, column=0, sticky = (N, S ,W ,E))
        #self.masterContainer.rowconfigure(2, weight=1)
        self.masterContainer.rowconfigure(3, weight=1)
        self.masterContainer.rowconfigure(10, weight=1)

        self.linesSettingsFrame = tk.Frame(self.masterContainer, bg="dark gray")
        self.linesSettingsFrame.grid(row=3,column=0,sticky=(N), columnspan=2)

        self.addRemoveButtonsContainer = tk.Frame(self.masterContainer, bg="dark gray")
        self.addRemoveButtonsContainer.grid(row=2, column=0, sticky=(N,E,W), columnspan=2)        


        self.nameLabels = []
        self.nameInputs = []
        self.axisComboboxes = []
        self.colorButtons = []
        
        self.baudrateCombobox = None

    def draw(self):


        openFileButton = tk.Button(self.masterContainer, text="Open File", command=self.controller.openFile)
        openFileButton.grid(padx=10,pady=20, row=0, column=0, sticky=(N, W))    
        
        self.linesSettings = self.controller.genLineSettings()

        for index, line in enumerate(self.linesSettings):

            if not line.visibility: #če črta obstaja ampak jo je treba skrit
                self.nameLabels[index].grid_remove()
                self.nameInputs[index].grid_remove()
                self.axisComboboxes[index].grid_remove()
                self.colorButtons[index].grid_remove()

            elif index+1 > len(self.nameLabels) and line.visibility: #če je črta nova in mora biti vidna naredi novo
            
                padx=10
                pady=3
                nameLabel = tk.Label(self.linesSettingsFrame, text= line.name)
                nameLabel.grid(row=index,column=0,pady=pady,padx=padx)
                self.nameLabels.append(nameLabel)

                nameInput = tk.Entry(self.linesSettingsFrame)
                nameInput.insert(0,line.name)
                nameInput.grid(row=index, column=1, pady=pady, padx=padx)
                self.nameInputs.append(nameInput)

                axisCombobox = Combobox(self.linesSettingsFrame, width=3, state="readonly", values=defaults.axisOptions)
                axisCombobox.set(line.axis)
                axisCombobox.grid(row=index, column=2, pady=pady, padx=padx)
                self.axisComboboxes.append(axisCombobox)

                #print(line.color)
                colorButton = tk.Button(self.linesSettingsFrame, text="Choose color", bg=line.color)
                colorButton.bind('<Button-1>', self.chooseColor)
                colorButton.grid(row=index, column=3, padx=padx, pady=pady)
                self.colorButtons.append(colorButton)

            else: #če črta že obstaja, je skrita in jo je treba odkrit
                padx=10
                pady=3
                self.nameLabels[index].grid(row=index, column=0,pady=pady,padx=padx)
                self.nameInputs[index].grid(row=index, column=1,pady=pady,padx=padx)
                self.axisComboboxes[index].grid(row=index, column=2,pady=pady,padx=padx)
                self.colorButtons[index].grid(row=index, column=3,pady=pady,padx=padx)


        addLineButton = tk.Button(self.addRemoveButtonsContainer, text=" + ", command=self.controller.addLine)
        addLineButton.grid(row=0, column=0, sticky=(N,S,W,E), padx=10, pady=20)

        removeLineButton = tk.Button(self.addRemoveButtonsContainer, text="  -  ", command=self.controller.removeLine)
        removeLineButton.grid(row=0, column=1, sticky=(N,S,W,E), padx=10, pady=20)



        goToNextPageButton = tk.Button(self.masterContainer, text="Go to graph page", command=lambda:self.controller.goToGraphPage())
        goToNextPageButton.grid(column=0, row=10, sticky = (W, S), pady=20, padx=10)

        label = tk.Label(self.masterContainer, text="Choose baudrate")
        label.grid(column=0, row=1, padx=10, sticky=(W,E))

        self.baudrateCombobox = Combobox(self.masterContainer, state="readonly", values=defaults.baudrates)
        self.baudrateCombobox.set(self.controller.loadBaudrateFromCache(defaults.cachedSettingsPath))
        self.baudrateCombobox.grid(column=1, row=1, sticky=(N,S,W,E))

    def getData(self):
        labels, names, axes, colors = [], [], [], []
        for index, value in enumerate(self.nameLabels):
            if  self.linesSettings[index].visibility: 
                labels.append(self.nameLabels[index]['text']) 
                names.append(self.nameInputs[index].get())
                axes.append(self.axisComboboxes[index].get())
                colors.append(self.colorButtons[index]['background'])
        #print("get data:" + str([labels, names, axes, colors]))
        return[[labels, names, axes, colors], self.baudrateCombobox.get()]

    def chooseColor(self,event):
        color = askcolor()[1]
        rowOfCallerButton = int(event.widget.grid_info()["row"])
        #print()
        button = self.colorButtons[rowOfCallerButton]
        #print("got to here")
        button.configure(background=color)
