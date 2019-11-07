import tkinter as tk
from tkinter import N,S,W,E


class graphView(tk.Frame):
    def __init__(self, parent, frame):
        tk.Frame.__init__(self,parent)

        container = tk.Frame(frame, bg="green")
        container.grid(row=0, column=0, sticky = (N, S ,W ,E))

        Button = tk.Button(container, text="neki neki na graph viewvu", command=lambda:parent.showPage("setup", frame))
        Button.grid(padx=10,pady=10, row=0, column=0)   