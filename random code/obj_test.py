from tkinter.ttk import *
import tkinter as ttk
from tkinter import N,S,W,E
#from tkinter import *

class MainPage(ttk.Tk):

    def __init__(self, *args, **kwargs):
        ttk.Tk.__init__(self,*args,*kwargs)
        container = ttk.Frame(self)
        container.grid(column=0,row=0,sticky=(N,S,W,E))
        container.configure(background="blue", borderwidth=10)
       #self.showFrame(container)
        #label = ttk.Label(self,text="neki123")
        #label.grid(column=0,row=0)
        #print("obj initialized")
        button = ttk.Button(container,text="nekibutton",command= lambda: self.deleteNekiPage(container))
        button.grid(column=0,row=0)

        nekiPage = NekiPage(container,self)

        #self.showFrame(nekiPage)

    def deleteNekiPage(self,container,*args):
        for arg in args:
            print(arg)

        self.nekiPage = None
        
        nekiPage = NekiPage(container,self)
        self.showFrame(nekiPage)
        

        
    def showFrame(self,frame):
        frame.grid(row=0,column=0,sticky=(N,S,W,E))
        frame.tkraise()


class NekiPage(ttk.Frame):
    
    def __init__(self,parent,controller):
        ttk.Frame.__init__(self,parent)

        label = ttk.Label(self, text="Start Page")
        label.grid(column=0,row=0,sticky=(E)) 
        nekiButton = ttk.Button(self,text="testButton123",command=self.deleteMe)
        nekiButton.grid(column=0,row=0)
        print("nekiPage Initialized")  

    def deleteMe(self):
        if self:
            self.destroy()


page = MainPage()
page.columnconfigure(0,weight=1)
page.rowconfigure(0,weight=1)

print("neki")
page.mainloop()

