
import tkinter
import tkinter as ttk
from tkinter import N,S,E,W

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
        container = ttk.Frame(self)
        container.grid(row=0,column=0,sticky = (N,S,E,W))
        container.rowconfigure(0,weight=1)
        container.columnconfigure(0,weight=1)

#frames manager setup
        self.frameNames = [SP.setupPage,MP.mainPage]
        self.frames = {}

        data = []

        mainPageObj = MP.mainPage(container, self, data) #container je parent frejma, self je controller, data je refference na graph Lines
        self.frames[MP.mainPage] = mainPageObj
        mainPageObj.grid(row=0,column=0,sticky=(N,S,W,E))
        mainPageObj.rowconfigure(0,weight=1)
        mainPageObj.columnconfigure(0,weight=1)

        serialReader = SerialReader.SerialRead(data, mainPageObj)
        serialReader.daemon = True
        serialReader.start()

        setupPageObj = SP.setupPage(container, self, data)
        self.frames[SP.setupPage] = setupPageObj
        setupPageObj.grid(row=0, column=0, sticky=(N,S,W,E))
        setupPageObj.rowconfigure(0,weight=1)
        setupPageObj.columnconfigure(0,weight=1)


        self.showFrame(SP.setupPage) #initiall page je setupPage


    def showFrame(self,frameToShowName):
        frame = self.frames[frameToShowName]
        frame.lift()


"""
        for F in (self.frameNames):
            if F == MP.mainPage:
                data = GraphLine.GraphLine("red",0)
                frame = F(container,self,data)

                serialReader = SerialReader.SerialRead(data,frame)
                serialReader.daemon = True
                serialReader.start()
            else:
                frame = F(container,self) #container je parent frejma, self je pa controller frejma
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky=(N,S,W,E))
            frame.rowconfigure(0,weight=1)
            frame.columnconfigure(0,weight=1)
"""
       





def main():
    app = measureGUI()
    app.rowconfigure(0,weight=1)
    app.columnconfigure(0,weight=1)
    app.geometry("1000x500")
    app.mainloop()

if __name__ == "__main__":
    main()