import tkinter as tk
import container as ct
from tkinter import N, S, W, E


class measureGUI(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs) 
        tk.Tk.wm_title(self,"measureGUI")

        container = ct.container(self)
        container.grid(row=0, column=0, sticky = (N,S,E,W))
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        consoleFrame = tk.Frame(container, height=100)
        consoleFrame.grid(row=1,column=0,sticky=(N,S,W,E))
        consoleFrame.columnconfigure(0,weight=1)
        consoleFrame.columnconfigure(2,weight=1)
        consoleFrame.rowconfigure(0,weight=1)
        consoleFrame.grid_propagate(False)
        container.showPage("console", consoleFrame)

        mainFrame = tk.Frame(container)
        mainFrame.grid(row=0,column=0,sticky = (N,S,E,W))
        mainFrame.rowconfigure(0,weight=1)
        mainFrame.columnconfigure(0,weight=1)


        container.showPage("setup", mainFrame)
        
        



if __name__ == "__main__":
    app = measureGUI()
    app.rowconfigure(0,weight=1)
    app.columnconfigure(0,weight=1)
    app.geometry("1500x750")
    app.mainloop()