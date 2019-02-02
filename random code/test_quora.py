from tkinter import *
from random import randint
 
from queue import Queue
# these two imports are important
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import time
import threading
 
continuePlotting = False
q = Queue()


def change_state():
    global continuePlotting
    if continuePlotting == True:
        continuePlotting = False
    else:
        continuePlotting = True
    
 
def data_points():
    f = open("data.txt", "w")
    for i in range(10):
        f.write(str(randint(0, 10   ))+'\n')
    f.close()
 
    f = open("data.txt", "r")
    data = f.readlines()
    f.close()
 
    l = []
    for i in range(len(data)):
        l.append(int(data[i].rstrip("\n")))
    return l
 
def app(in_q):
    # initialise a window.

    print("app called")
    root = Tk()
    root.config(background='white')
    root.geometry("1000x700")
    
    lab = Label(root, text="Live Plotting", bg = 'white')
    lab.pack()
    
    fig = Figure(figsize=(5,5), dpi=100)
    
    ax = fig.add_subplot(111)
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.grid()
 
    graph = FigureCanvasTkAgg(fig, master=root)
    graph.get_tk_widget().pack(side="top",fill='both',expand=True)
 

    h = in_q.get()
    prin("neki")
    updateGraph(h)

    print("called updategraph from app() with:" + h)
    '''
    def plotter():
        while continuePlotting:
            ax.clear()
            ax.grid()
            dpts = data_points()
            print(dpts)
            ax.plot([0,1,2,3,4,5,6,7,8,9], dpts)
            #graph.draw()
            time.sleep(1)
    '''       

    def getData(out_q):
        print("getdata called")
        while continuePlotting:
            data = data_points()
            time.sleep(1)
            out_q.put(data)

    def updateGraph(data):
        print("updategraph called")
        ax.clear()
        ax.grid()
        dpts = data_points()
        print(dpts)
        ax.plot([0,1,2,3,4,5,6,7,8,9], dpts)
        #graph.draw()
        time.sleep(1)


    def gui_handler():
        change_state()
        print("gui_handler called")
        #plotter()
        t = threading.Thread(target=getData, args=(q,))
        t.start()
        q.join()
        #t.join()
 





    b = Button(root, text="Start/Stop", command=gui_handler, bg="red", fg="white")
    b.pack()
    root.update()
    root.mainloop()
 
if __name__ == '__main__':
    print("main started")
    mainThread = threading.Thread(target=app,args=(q,))
    #mainThread.daemon = False
    mainThread.start()


    #randomThread.join()
    #app()