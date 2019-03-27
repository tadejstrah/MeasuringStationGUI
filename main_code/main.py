
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
        self.container = ttk.Frame(self)
        self.container.grid(row=0,column=0,sticky = (N,S,E,W))
        self.container.rowconfigure(0,weight=1)
        self.container.columnconfigure(0,weight=1)

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


        #pass

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