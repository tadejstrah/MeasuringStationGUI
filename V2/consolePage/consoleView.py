import tkinter as tk
from tkinter import N,S,W,E

class consoleView(tk.Frame):
    def __init__(self,parent,frame):
        tk.Frame.__init__(self,parent)
        print("consoleView sucessfully inited")
        openFileButton = tk.Button(self, text="Open neki", command=None)
        openFileButton.grid(padx=10,pady=10, row=0, column=0)    
        

        self.dataConsole = tk.Text(frame, borderwidth=3, state="normal")
        self.dataConsole.config(undo=True,wrap="word")
        self.dataConsole.grid(row=0,column=0,sticky=(S,W,E),padx=2,pady=2)


        self.notificationsConsole = tk.Text(frame,borderwidth=3,state="disabled")
        self.notificationsConsole.config(undo=True,wrap="word")
        self.notificationsConsole.grid(row=0,column=2,sticky=(S,W,E), padx=2,pady=2)

        scrollbar1 = tk.Scrollbar(frame,command=self.dataConsole.yview)
        scrollbar1.grid(row=0,column=1,sticky=(N,S,W,E))
        self.dataConsole["yscrollcommand"] = scrollbar1.set

        scrollbar2 = tk.Scrollbar(frame,command=self.notificationsConsole.yview)
        scrollbar2.grid(row=0,column=3,sticky=(N,S,W,E))
        self.notificationsConsole["yscrollcommand"] = scrollbar2.set
