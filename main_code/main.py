
import tkinter
import tkinter as ttk
from tkinter import N,S,E,W,END,INSERT


import setupPage as SP
import mainPage as MP 
import SerialReader
import time
import GraphLine

class measureGUI(ttk.Tk):
    def __init__(self,*args,**kwargs):
        ttk.Tk.__init__(self,*args,**kwargs)
        ttk.Tk.wm_title(self,"measureGUI")

#container frame setup
        self.container = ttk.Frame(self)
        self.container.grid(row=0,column=0,sticky = (N,S,E,W))
        self.container.rowconfigure(0,weight=1)
        self.container.columnconfigure(0,weight=1)

        self.printConsole = ttk.Frame(self,height=100)
        self.printConsole.grid(row=1,column=0,sticky=(N,S,W,E))
        self.printConsole.columnconfigure(0,weight=1)
        self.printConsole.rowconfigure(0,weight=1)
        self.printConsole.grid_propagate(False)

        text = ttk.Text(self.printConsole,borderwidth=3,state="disabled")
        text.config(undo=True,wrap="word")
        text.grid(row=0,column=0,sticky=(S,W,E),padx=2,pady=2)
        text.configure(state="normal")
        text.insert(END,"Hello World\n")
        text.insert(END,"This is print console \nImportant information will be displayed here in the future")
        text.configure(state="disabled")

        scrollbar = ttk.Scrollbar(self.printConsole,command=text.yview)
        scrollbar.grid(row=0,column=1,sticky=(N,S,W,E))
        text["yscrollcommand"] = scrollbar.set

#frames manager setup
        self.frameNames = [SP.setupPage,MP.mainPage]
        self.frames = {}

        self.data = []


        setupPageObj = SP.setupPage(self.container, self, self.data)
        self.frames[SP.setupPage] = setupPageObj
        setupPageObj.grid(row=0, column=0, sticky=(N,S,W,E))
        setupPageObj.rowconfigure(0,weight=1)
        setupPageObj.columnconfigure(0,weight=1)

        #self.serialReader = None
       # self.initMainPage()


        self.showFrame(SP.setupPage) #initiall page je setupPage

    def showFrame(self,frameToShowName):
        #print(frameToShowName)
        #print(self.frames.keys())
        frame = self.frames[frameToShowName]
        frame.lift()

    def initMainPage(self):
        #("init main page")
        mainPageObj = MP.mainPage(self.container, self, self.data) #container je parent frejma, self je controller, data je refference na graph Lines
        self.frames[MP.mainPage] = mainPageObj
        mainPageObj.grid(row=0,column=0,sticky=(N,S,W,E))
        mainPageObj.rowconfigure(0,weight=1)
        mainPageObj.columnconfigure(0,weight=1)
          
        serialReader = SerialReader.SerialRead(self.data, mainPageObj)
        serialReader.daemon = True
        serialReader.start()


def main():
    app = measureGUI()
    app.rowconfigure(0,weight=1)
    app.columnconfigure(0,weight=1)
    app.geometry("1000x500")
    app.mainloop()

if __name__ == "__main__":
    main()