import tkinter as tk
from tkinter import N,S,W,E


class setupView(tk.Frame):
    def __init__(self, parent, frame):
        tk.Frame.__init__(self,parent)
        print("setupView sucessfully inited")

        container = tk.Frame(frame, bg="red")
        container.grid(row=0, column=0, sticky = (N, S ,W ,E))

        openFileButton = tk.Button(container, text="Open File", command=lambda:parent.showPage("graph", frame))
        openFileButton.grid(padx=10,pady=10, row=0, column=0)    
        