import tkinter as tk
from tkinter import N,S,W,E
from tkinter.ttk import Combobox


class setupView(tk.Frame):
    def __init__(self, parent, frame):
        tk.Frame.__init__(self,parent)

        self.parent = parent
        self.controller = None

        self.linesSettings = []


        self.masterContainer = tk.Frame(self, bg="red")
        self.masterContainer.grid(row=0, column=0, sticky = (N, S ,W ,E))

        self.nameLabels = []
        self.nameInputs = []
        self.axisComboboxes = []
        self.colorComboboxes = []
        #self.visibility = []
        

    def draw(self):
        openFileButton = tk.Button(self.masterContainer, text="Open File", command=lambda:self.parent.showPage("graph", self))
        openFileButton.grid(padx=10,pady=10, row=0, column=0)    
        
        self.linesSettings = self.controller.genLineSettings()
        for index, line in enumerate(self.linesSettings):
            nameLabel = tk.Label(self, text= str(index) + " Label")
            nameLabel.grid(row=index+1,column=0,pady=3,padx=10)
            self.nameLabels.append(nameLabel)

        
        #nrOfLinesOptions = [i for i in (range(1,10))]
        #nrOfLinesCombobox = Combobox(self.container, values=nrOfLinesOptions, state="readonly")
        #nrOfLinesCombobox.set() #setting default value
        #nrOfLinesCombobox.bind('<<ComboboxSelected>>', self.on_dropDownMenu_select) #binding 
        #nrOfLinesCombobox.grid()
        #print(self.controller.genLineSettings())


    def drawLinesSettings(self, ):
        pass