import tkinter as tk
import importlib


class container(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self,parent)
        self.__frames = {}
        self.__frameNames = ["setup","graph"] #string names
        self.__initedFrameNames = []

    def showPage(self,name,frame):
        print()
        print("showPage: " + name)
        if name in self.__initedFrameNames:
            #print(frame)
            self.__frames[name][1].tkraise()
            self.__frames[name][1].grid(row=0, column=0, sticky = "N S W E")

        else:
            page = self.__initPage(name, frame)
            self.__initedFrameNames.append(name)
            self.__frames[name][1].tkraise()




    def __initPage(self,name,frame):

        viewPackage = importlib.import_module("." + str(name) + "View", name+"Page")
        viewClass = getattr(viewPackage,name + "View")

        controllerPackage = importlib.import_module("." + str(name) + "Controller", name+"Page")
        controllerClass = getattr(controllerPackage,name + "Controller")

        initedView = viewClass(self,frame)
        initedView.grid(row=0, column=0, sticky= "N S W E")
        initedView.rowconfigure(0,weight=1)
        initedView.columnconfigure(0,weight=1)
        print("InitedView: " + str(initedView))
        
        initedController = controllerClass(initedView, self)
        #initedView.controller = initedController
        
        self.__frames[name] = (initedController, initedView,)
        return initedView

    def getControllerRefferenceOf(self, name):
        return self.__frames[name][0]
                             

