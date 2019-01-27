import tkinter as tk
from tkinter import N,S,E,W


LARGE_FONT= ("Verdana", 12)

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        #container.pack(side="top", fill="both", expand = True)
        container.grid(column=0,row=0,sticky=(N,E,S,W))
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.configure(background="red",borderwidth=10)
        
        self.frames = {}

        frame = StartPage(container, self)

        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky=(N,E,S,W))

        self.show_frame(StartPage)
    
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.grid(column=0,row=0,sticky=(E))
       # label.pack(pady=10,padx=10)

app = SeaofBTCapp()
app.columnconfigure(0,weight=1)
app.rowconfigure(0,weight=1)
app.mainloop()