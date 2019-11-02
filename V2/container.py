import tkinter as tk
import importlib


class container(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self,parent)
        self.__frames = {}
        self.__frameNames = ["setup","graph"] #string names
        self.__initedFrameNames = []

    def showPage(self,name,frame):
        print("showPage: " + name)
        if name in self.__initedFrameNames:
            self.__frames[name][1].frame = frame
            self.__frames[name][1].lift()
            print(self.__frames)

        else:
            page = self.__initPage(name, frame)
            page.lift()
            self.__initedFrameNames.append(name)
            #print(self.__initedFrameNames)



    def __initPage(self,name,frame):

        viewPackage = importlib.import_module("." + str(name) + "View", name+"Page")
        viewClass = getattr(viewPackage,name + "View")

        controllerPackage = importlib.import_module("." + str(name) + "Controller", name+"Page")
        controllerClass = getattr(controllerPackage,name + "Controller")

        modelPackage = importlib.import_module("." + str(name) + "Model", name+"Page")
        modelClass = getattr(modelPackage,name + "Model")

        initedModel = modelClass()
        initedView = viewClass(self,frame)
        initedView.grid(row=0, column=0)
        initedView.rowconfigure(0,weight=1)
        initedView.columnconfigure(0,weight=1)
        
        initedController = controllerClass(initedView, initedModel)
        self.__frames[name] = (initedController, initedView, initedModel,)
        return initedView


    def getControllerRefferenceOf(self, name):
        return self.__frames[name][0]
                             

