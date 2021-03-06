import tkinter as tk
from tkinter import N,S,W,E,END

class consoleView(tk.Frame):
    def __init__(self,parent,frame):
        tk.Frame.__init__(self,parent)

        self.controller = None
        self.frame = frame
        #print("consoleView sucessfully inited")
 

    def draw(self):
        openFileButton = tk.Button(self, text="Open neki", command=None)
        openFileButton.grid(padx=10,pady=10, row=0, column=0)    
        

        self.dataConsole = tk.Text(self.frame, borderwidth=3, state="normal")
        self.dataConsole.config(undo=True,wrap="word")
        self.dataConsole.grid(row=0,column=0,sticky=(S,W,E),padx=2,pady=2)


        self.notificationsConsole = tk.Text(self.frame,borderwidth=3,state="disabled")
        self.notificationsConsole.config(undo=True,wrap="word")
        self.notificationsConsole.grid(row=0,column=2,sticky=(S,W,E), padx=2,pady=2)

        dataConsoleScrollbar = tk.Scrollbar(self.frame,command=self.dataConsole.yview)
        dataConsoleScrollbar.grid(row=0,column=1,sticky=(N,S,W,E))
        self.dataConsole["yscrollcommand"] = dataConsoleScrollbar.set

        notificationConsoleScrollbar = tk.Scrollbar(self.frame,command=self.notificationsConsole.yview)
        notificationConsoleScrollbar.grid(row=0,column=3,sticky=(N,S,W,E))
        self.notificationsConsole["yscrollcommand"] = notificationConsoleScrollbar.set

    def printToLeftConsole(self, string):
        #self.dataConsole.configure(state = "normal") #changing state with every write cycle slows down the program dramatically. I will just have to live with the state being on normal all the time
        self.dataConsole.insert(END, string + "\n")
        self.dataConsole.see("end")
        #self.dataConsole.configure(state="disabled")

    def printToRightConsole(self, string):
        self.notificationsConsole.configure(state="normal")
        self.notificationsConsole.insert(END, string + "\n")
        self.notificationsConsole.see("end")
        self.notificationsConsole.configure(state="disabled") 