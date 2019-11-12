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


        self.masterContainer = tk.Frame(self, bg="red")
        self.masterContainer.grid(row=0, column=0, sticky = (N, S ,W ,E))

        self.linesSettingsFrame = tk.Frame(self.masterContainer)
        self.linesSettingsFrame.grid(column=0,row=1,sticky=(N,S,W,E))


        self.nameLabels = []
        self.nameInputs = []
        self.axisComboboxes = []
        self.colorButtons = []
        

    def draw(self):
        openFileButton = tk.Button(self.masterContainer, text="Open File", command=lambda:self.parent.showPage("graph", self))
        openFileButton.grid(padx=10,pady=10, row=0, column=0)    
        
        self.linesSettings = self.controller.genLineSettings()

        for index, line in enumerate(self.linesSettings):
            nameLabel = tk.Label(self.linesSettingsFrame, text= "Label " + str(index))
            nameLabel.grid(row=index,column=0,pady=3,padx=10)
            self.nameLabels.append(nameLabel)

            nameInput = tk.Entry(self.linesSettingsFrame)
            nameInput.insert(0,"Label  " +str(index+1))
            nameInput.grid(row=index, column=1, pady=3, padx=10)
            self.nameInputs.append(nameInput)

            axisCombobox = Combobox(self.linesSettingsFrame, width=3, state="readonly", values=defaults.axisOptions)
            axisCombobox.set(defaults.axisOptions[0])
            axisCombobox.grid(row=index, column=2, pady=3, padx=10)
            self.axisComboboxes.append(axisCombobox)

            colorButton = tk.Button(self.linesSettingsFrame, text="Choose color", bg=defaults.predefinedColors[index])
            colorButton.bind('<Button-1>', self.chooseColor)
            colorButton.grid(row=index, column=3, padx=10, pady=3)
            self.colorButtons.append(colorButton)


    def chooseColor(self,event):
        color = askcolor()[1]
        #print(color)
        rowOfCallerButton = int(event.widget.grid_info()["row"])
        self.colorButtons[rowOfCallerButton].configure(background=color)
        #self.colorButtons[rowOfCallerButton].config(relief=RAISED)
        #print(self.colorButtons[rowOfCallerButton].cget('bg'))

    def drawLinesSettings(self, ):
        pass