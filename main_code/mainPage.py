
import tkinter
import tkinter as ttk
import setupPage as SP

class mainPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self,parent)

        testLabel = ttk.Label(self,text="test label on main page")
        testLabel.grid()

        testButton = ttk.Button(self, text="test button on main page",command=lambda:controller.showFrame(SP.setupPage))
        testButton.grid()