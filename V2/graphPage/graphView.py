import tkinter as tk
from tkinter import N,S,W,E


class graphView(tk.Frame):
    def __init__(self, parent, frame):
        tk.Frame.__init__(self,parent)

        self.parent = parent
        self.controller = None



        self.container = tk.Frame(self, bg="green")
        self.container.grid(row=0, column=0, sticky = (N, S ,W ,E))

 

    def draw(self):
        Button = tk.Button(self.container, text="neki neki na graph viewvu", command=lambda:self.parent.showPage("setup", self))
        Button.grid(padx=10,pady=10, row=0, column=0)              