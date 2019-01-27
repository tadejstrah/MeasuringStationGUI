
from tkinter import *
from tkinter.ttk import * 
from tkinter import ttk

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg#, NavigationToolbar2TkAgg
from matplotlib.figure import Figure


root = Tk()
root.title("Serial to graph")

s = Style()
s.configure("TFrame", background="red")
#s.configure("TLabel",backgorund="blue")

root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)
root.configure(background="blue")

mainframe = ttk.Frame(root,style="TFrame", borderwidth=0) #red red red red red
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))    
mainframe.columnconfigure(0,weight=1)
mainframe.rowconfigure(0,weight=1)


s2 = Style()
s2.configure("neki.TFrame",background="yellow")
testFrame = ttk.Frame(mainframe,style="neki.TFrame",padding="100 100 100 100")
testFrame.grid(column=1,row=0,sticky=(N,S))
 
#testFrame.pack(side=LEFT,expand=YES,fill=BOTH)

s3 = Style()
s3.configure("bhus.TFrame",background="green")
testFrame2=ttk.Frame(mainframe,style="bhus.TFrame")
testFrame2.grid(column=0,row=0,sticky=(N,E,S,W))
testFrame2.rowconfigure(0,weight=1)
testFrame2.columnconfigure(0,weight=1)

ttk.Label(testFrame2,text="shdikjgndls",background="white",padding="100 100 100 100").grid(column=0,row=0,sticky=(N,S,W,E))

ttk.Label(testFrame,text="nekineki",background="purple").grid(column=0,row=0)


f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)
a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])

canvas = FigureCanvasTkAgg(f,master=testFrame2)
canvas.get_tk_widget().grid(column=0,row=0,sticky=(N,S,W,E))
# canvas.show()
#canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

#toolbar = NavigationToolbar2TkAgg(canvas, self)
# toolbar.update()
#canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)












root.mainloop()