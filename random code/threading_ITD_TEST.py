import threading
import time
from queue import Queue
from random import randint

from tkinter import *

from matplotlib import pyplot as plt
import matplotlib.animation as animation

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

q = Queue()
#q.put("neki")



root = Tk()
root.geometry('1200x700+200+100')
root.title('This is my root window')
root.state('zoomed')
root.config(background='#fafafa')


xar = []
yar = []

fig = plt.figure(figsize=(14, 4.5), dpi=100)
ax1 = fig.add_subplot(1, 1, 1)
ax1.set_ylim(0, 100)
line, = ax1.plot(xar, yar, 'r', marker='o')



def animate(interval,*fargs):
    try:
        neki = fargs[0].get()
        print(neki)
        yar.append(neki)
        xar.append(interval)
        line.set_data(xar,yar)
        ax1.set_xlim(0,interval+1)
    except:
        print("queue ne dela")


def getRandomData(queue):
    while True:
        queue.put(randint(0,100))
        print("getrndomdata")
        time.sleep(0.1)

plotcanvas = FigureCanvasTkAgg(fig, root)
plotcanvas.get_tk_widget().grid(column=1, row=1)
ani = animation.FuncAnimation(fig, animate ,fargs=(q,),interval=100, blit=False)

randomThread = threading.Thread(target=getRandomData, args=(q,) )
randomThread.start()


root.mainloop()