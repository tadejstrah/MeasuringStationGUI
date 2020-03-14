import defaults
import setupPage.lineSettings
import json

import easygui

class setupController():
    def __init__(self, view, parent):
        self.view = view
        view.controller = self
        self.parent = parent
        self.generatedLinesSettings = []

        self.consoleController = parent.getControllerRefferenceOf("console")
        view.draw()


    def genLineSettings(self):
        if (len(self.generatedLinesSettings) > 0): return self.generatedLinesSettings #če lajn settingsi že obstajajo (goin from graph to setup and so on) jih samo returna

        if self.cacheExists(defaults.cachedSettingsPath): #če cache file obstaja ga naloži
            self.consoleController.printToRightConsole("Cache file found, loading settings")
            cachedData = self.loadCachedLineSettings(defaults.cachedSettingsPath)
            for index in range(len(cachedData[0])): #zgenerira lineSettings objecte iz cacha
                name = cachedData[0][index]
                color = cachedData[3][index]
                visibility = True
                axis = cachedData[2][index]
                lineSetting = setupPage.lineSettings(name, color, visibility, axis, index)
                self.generatedLinesSettings.append(lineSetting)
            return self.generatedLinesSettings
        else: #če cache ne obstaja zgenerira default
            self.consoleController.printToRightConsole("Cache file not found at default location, loading default settings")
            for i in range(defaults.initialNrOfLineSettings):
                lineSetting = setupPage.lineSettings("Line " + str(i), defaults.predefinedColors[i], True, defaults.axisOptions[0], i)
                self.generatedLinesSettings.append(lineSetting)
        return self.generatedLinesSettings

    

    def addLine(self): #dodaj line do te cifre ali jih samo make visible
        nrOfVisibleLines = sum(p.visibility == True for p in self.generatedLinesSettings)
        if nrOfVisibleLines==defaults.maxNrOfLines:
            self.consoleController.printToRightConsole("You have reached maximum number of lines: " + str(defaults.maxNrOfLines))
            return
        hiddenLinesExist = False
        for line in self.generatedLinesSettings:
            if not line.visibility and not hiddenLinesExist:
                line.visibility = True
                hiddenLinesExist = True
                break
        
        if not hiddenLinesExist:
            prevLineId = self.generatedLinesSettings[-1].id
            newLineSetting = setupPage.lineSettings("Line " + str(prevLineId + 1), defaults.predefinedColors[(prevLineId + 1)%len(defaults.predefinedColors)], True, defaults.axisOptions[0], prevLineId + 1)
            self.generatedLinesSettings.append(newLineSetting)
        self.view.draw()


    def removeLine(self): #removaj line/ make them not visible
        hiddenLinesExist = False
        nrOfVisibleLines = sum(p.visibility == True for p in self.generatedLinesSettings)
        if nrOfVisibleLines ==1: 
            self.consoleController.printToRightConsole("You mush have at least one line to draw on")
            self.view.draw()
            return

        for index, line in enumerate(reversed(self.generatedLinesSettings)):
            if not line.visibility:
                hiddenLinesExist = True
                if self.generatedLinesSettings[line.id-1].visibility == True:
                    self.generatedLinesSettings[line.id-1].visibility = False
                    break
   
        if not hiddenLinesExist:
            self.generatedLinesSettings[-1].visibility = False
        
        self.view.draw()
        


    def loadCachedLineSettings(self, path): 
        with open(path, mode="r") as cacheFile:
            jsonString = cacheFile.readline()
            #print(jsonString)
            cacheFile.close()
            return(json.loads(jsonString)[0])

    def loadBaudrateFromCache(self, path):
        if self.cacheExists(path): 
            with open(path, mode="r") as cacheFile:
                jsonString = cacheFile.readline()
                #print(jsonString)
                return(json.loads(jsonString)[1])
        else: 
            return 38400

    def cacheExists(self, path):
        try:
            with open(path) as file:
                file.close()
                return True
        except:
            return False

    def saveSettingsToCache(self, path, data):
        with open(path, mode="w") as cacheFile:
            jsonString = json.dumps(data)
            #print(jsonString)
            cacheFile.write(jsonString)
            cacheFile.close()


    def openFile(self):

        openFileName = easygui.fileopenbox()

        with open (openFileName, mode="r") as inputFile:
            jsonString = inputFile.readline()
            temp = json.loads(jsonString)
            data = temp[0]
            time = temp[1]
            #print(jsonString)

            labels = []
            names = []
            axes = []
            colors = []
            values = []
            for line in data:
                #print(line)
                labels.append(line[1])
                names.append(line[1])
                axes.append(line[2])
                colors.append(line[3])
                values.append(line[4])
            
        self.goToGraphPage(openFileLinesData = [labels, names, axes, colors], valuesData=[values, time])


    def goToGraphPage(self, **kwargs):
        values = None
        time = None
        if "openFileLinesData" in kwargs.keys():
            if kwargs["openFileLinesData"] != None:
                data = [kwargs["openFileLinesData"], self.view.getData()[1]]
                #print(self.view.getData()[1])
            else: data = []

        if "valuesData" in kwargs.keys():
            if kwargs["valuesData"] != None:
                #print(kwargs["valuesData"])
                values = kwargs["valuesData"][0]
                time = kwargs["valuesData"][1]

                # print(kwargs["valuesData"])
                #data = [kwargs["valuesData"], self.view.getData()[1]]
                #print(self.view.getData()[1])
            else: data = []     

        else:
            data = self.view.getData()  #return[[labels, names, axes, colors], self.baudrateCombobox.get()]
 

        self.saveSettingsToCache(defaults.cachedSettingsPath,data)
        self.parent.showPage("graph", self.view) #inits and transitions

        if values != None:
            self.parent.getControllerRefferenceOf("graph").setData(data, values=[values, time])
        else:
            self.parent.getControllerRefferenceOf("graph").setData(data)
        