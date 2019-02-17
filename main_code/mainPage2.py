
from tkinter import *
import tkinter as ttk
import setupPage as SP
from random import randint

#from matplotlib import pyplot as plt
#plt.close()
import matplotlib

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import threading
import time
from queue import Queue


q = Queue()
q.put(10)
c =0

xar = [0,1,2]
yar = [0,1,43]

fig = plt.Figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_ylim(0,100)
ax1.set_xlim(0,10)
#ax1.plot(xar,yar)
line, = ax1.plot(xar,yar,'r',marker='o')
line.set_data(xar,yar)

class mainPage(ttk.Frame):

    #q = Queue()
    #q.put("neki")
    #xar = []
    #yar= []
    #ax1 = None
    #neki = 0

    def animate2(self):
        print("animate2")


   # def plotToGraph(self,graph,xar,yar):
    #    graph.plot(xar,yar)
#
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self,parent)

        testLabel = ttk.Label(self,text="test label on main page")
        testLabel.grid()

        testButton = ttk.Button(self, text="test button on main page",command=lambda:controller.showFrame(SP.setupPage))
        testButton.grid() 

        #self.q = Queue()

        self.c = 0
        #print(ax1)
        #self.line, = ax1.plot(xar,yar,'r',marker='o', animated=True)
        #self.plotToGraph(ax1,xar,yar)
        #ax1.plot([1,2,34,2,3,4])
        #self.line.set_data([1,2,3,4,5,6],[3,5,3,54,32,4])

        #print(fig)
        
        plotcanvas = FigureCanvasTkAgg(fig, parent)
        plotcanvas.get_tk_widget().grid(column=0,row=4)

        #!!!! namesto funcAnimation probej timer narest ¸

        #self.animate(1,q,None,ax1,c)
        #breakpoint()
        ani = animation.FuncAnimation(fig,self.animate, fargs=(q,),interval=10,repeat=True,blit=True)

        #ani = animation.FuncAnimation(fig, animate, fargs=(self.q,), interval=1,blit=False)
        #ani2 = animation.FuncAnimation(fig, self.animate2, interval = 1)
        #self.q.put("neki")
        #print(self.q.get())
        #print(ani)
        #breakpoint()
        testThread = threading.Thread(target=self.serialRead,args=(q,))
        testThread.daemon=True
        testThread.start()

        time.sleep(0.1)

        line.set_data([1,2,3,4,5,6],[8,6,4,2,4,3])
        #breakpoint()
       # print("pršu mim startanja novga threda")


    def shouldSerialRead(self):
        return True
    

    def serialRead(self,queue):
        while self.shouldSerialRead():
            queue.put(randint(0,100))
            #print("serial reading")
            #print(queue.empty())
            time.sleep(0.1)


    def animate(self,interval,*fargs):
        #breakpoint()
        #print("animate called")
        
        if not q.empty():
            neki = q.get(block=False)
            #print(neki)
            yar.append(int(neki))
            xar.append(interval)
            #print("fargs[2]")
            #print(ax1)

            #print(yar)


        nekiXYZ = [0,1,2,3,40]
        
        #ax1.plot(nekiXYZ)
        #if len(yar)>0:
        print(xar)
        print(yar)
        #plt.plot(yar)
        #plt.show()


        #for element in yar:
            #nekiXYZ.append(element)
         #   pass
            #ax1.plot([yar[0],45,3,43])

        #print(yar)

        #if self.c < 15:
        #    self.c += 1
        #else:
        #ax1.plot([0, 1, 58, 53, 60, 68, 6, 58])
        #ax1.plot(yar)
        #time.sleep(0.1)
        #ax1.pause(0.05)

        #ax1.plot([yar[0],2,4,3,1,4])
        #ax1.plot([1,54,3,interval,3])
        #print(xar)
        #print(yar)
        #ani = animation.FuncAnimation(fig,self.animate, fargs=(q,),interval=1,repeat=True)

        line.set_data(xar,yar)
        return line,
        #plt.plot(yar)
        #line.set_data([0,1,2,3,4],[0,1,4,9,16])     

        #print(type(ax1))
            #fargs[1].set_data(self.xar,self.yar)
        #print(q.qsize())
        #print(fargs[0].get())
        '''try:
            #neki = fargs[0].get()
            #neki = q.get()
            #print(neki)
        '''
        #print(fargs[3])


        #print(self.xar)
        #print(self.yar)
        #print(fargs)
        #print(interval)
        #fargs[2].set_xlim(0,interval+1)
        #    print("neki")
        #except:
        #    print("queue ne dela")
        #print("starting timer")
        #if interval < 10:

        '''
        timer = threading.Timer(0.5,lambda:self.animate(interval+1,fargs[0],fargs[1],fargs[2]))
        timer.daemon = True
        timer.start()
        '''