
import tkinter
import tkinter as ttk
from tkinter import N,S,E,W

import setupPage as SP
import mainPage as MP 


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
        for F in (self.frameNames):
            frame = F(container,self) #container je parent frejma, self je pa controller frejma
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky=(N,S,W,E))
            frame.rowconfigure(0,weight=1)
            frame.columnconfigure(0,weight=1)
        
        self.showFrame(SP.setupPage) #initiall page je setupPage
       
    def showFrame(self,frameToShowName):
        frame = self.frames[frameToShowName]
        frame.lift()




def main():
    app = measureGUI()
    app.rowconfigure(0,weight=1)
    app.columnconfigure(0,weight=1)
    app.geometry("400x400")
    app.mainloop()

if __name__ == "__main__":
    main()