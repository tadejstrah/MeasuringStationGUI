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
        button = ttk.Button(container,text="nekibutton",command=self.deleteNekiPage)
        button.grid(column=0,row=0)

        nekiPage = NekiPage(container,self)

        #self.showFrame(nekiPage)

    def deleteNekiPage(self,*args):
        for arg in args:
            print(arg)

        self.nekiPage = None

        nekiPage = NekiPage(self,self)
        self.showFrame(nekiPage)
        

        
    def showFrame(self,frame):
        frame.grid(row=1,column=0,sticky=(N,S,W,E))
        frame.tkraise()


class NekiPage(ttk.Frame):
    
    def __init__(self,parent,controller):
        ttk.Frame.__init__(self,parent)

        label = ttk.Label(self, text="Start Page")
        label.grid(column=3,row=0,sticky=(E)) 
        print("nekiPage Initialized")  


page = MainPage()
page.columnconfigure(0,weight=1)
page.rowconfigure(0,weight=1)

print("neki")
page.mainloop()

