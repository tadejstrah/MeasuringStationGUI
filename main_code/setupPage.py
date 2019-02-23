
import tkinter
import tkinter as ttk
from tkinter import N,S,W,E
import mainPage as MP

class setupPage(ttk.Frame):
    def __init__(self,parent,controller):
        ttk.Frame.__init__(self,parent)
        label = ttk.Label(self,text="test label on setup page",background="red")
        label.grid(column=0,row=0,sticky=(S,E,W,N))
        label2 = ttk.Label(self,text="lbael 2",background="blue")
        label2.grid()

        testButton = ttk.Button(self, text="gotomainpage",command=lambda:controller.showFrame(MP.mainPage))
        testButton.grid()

        

        
 
