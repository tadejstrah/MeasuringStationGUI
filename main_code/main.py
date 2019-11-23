
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

        #self.ser = None

#container frame setup
        self.container = ttk.Frame(self)
        self.container.grid(row=0,column=0,sticky = (N,S,E,W))
        self.container.rowconfigure(0,weight=1)
        self.container.columnconfigure(0,weight=1)

        self.printConsole = ttk.Frame(self,height=100)
        self.printConsole.grid(row=1,column=0,sticky=(N,S,W,E))
        self.printConsole.columnconfigure(0,weight=1)
        self.printConsole.columnconfigure(2,weight=1)
        self.printConsole.rowconfigure(0,weight=1)
        self.printConsole.grid_propagate(False)


        self.dataConsole = ttk.Text(self.printConsole, borderwidth=3, state="normal")
        self.dataConsole.config(undo=True,wrap="word")
        self.dataConsole.grid(row=0,column=0,sticky=(S,W,E),padx=2,pady=2)


        self.notificationsConsole = ttk.Text(self.printConsole,borderwidth=3,state="disabled")
        self.notificationsConsole.config(undo=True,wrap="word")
        self.notificationsConsole.grid(row=0,column=2,sticky=(S,W,E), padx=2,pady=2)

        scrollbar1 = ttk.Scrollbar(self.printConsole,command=self.dataConsole.yview)
        scrollbar1.grid(row=0,column=1,sticky=(N,S,W,E))
        self.dataConsole["yscrollcommand"] = scrollbar1.set

        scrollbar2 = ttk.Scrollbar(self.printConsole,command=self.notificationsConsole.yview)
        scrollbar2.grid(row=0,column=3,sticky=(N,S,W,E))
        self.notificationsConsole["yscrollcommand"] = scrollbar2.set

#frames manager setup
        self.frameNames = [SP.setupPage,MP.mainPage]
        self.frames = {}

        self.data = []


        setupPageObj = SP.setupPage(self.container, self, self.data)
        self.frames[SP.setupPage] = setupPageObj
        setupPageObj.grid(row=0, column=0, sticky=(N,S,W,E))
        setupPageObj.rowconfigure(0,weight=1)
        setupPageObj.columnconfigure(0,weight=1)
        setupPageObj.on_dropDownMenu_select(None)
        #self.serialReader = None
       # self.initMainPage()

 
        self.showFrame(SP.setupPage) #initiall page je setupPage

    def showFrame(self,frameToShowName):
        #print(frameToShowName)
        #print(self.frames.keys())
        frame = self.frames[frameToShowName]
        frame.lift()

    def initMainPage(self):

        self.serialReader = SerialReader.SerialRead(self.data,self)
        self.serialReader.daemon = True
    
        self.mainPageObj = MP.mainPage(self.container, self, self.data,self.serialReader) #container je parent frejma, self je controller, data je refference na graph Lines
        self.frames[MP.mainPage] = self.mainPageObj
        self.mainPageObj.grid(row=0,column=0,sticky=(N,S,W,E))
        self.mainPageObj.rowconfigure(0,weight=1)
        self.mainPageObj.columnconfigure(0,weight=1)
          
        self.serialReader.mainPageRefference = self.mainPageObj
        self.serialReader.start()

    def printToConsole(self,text,dataConsole):
        if dataConsole:
            #self.dataConsole.configure(state="normal")
            self.dataConsole.insert(END, text)
            self.dataConsole.see("end")
           # self.dataConsole.configure(state="disabled")
        else:
            self.notificationsConsole.configure(state="normal")
            self.notificationsConsole.insert(END, text)
            self.notificationsConsole.see("end")
            self.notificationsConsole.configure(state="disabled") 

#@line_profiler 
def main():
    app = measureGUI()
    app.rowconfigure(0,weight=1)
    app.columnconfigure(0,weight=1)
    app.geometry("1500x750")
    app.mainloop()


if __name__ == "__main__":
    main()