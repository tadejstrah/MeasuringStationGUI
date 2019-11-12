import defaults
import setupPage.lineSettings


class setupController():
    def __init__(self, view, parent):
        self.view = view
        view.controller = self

        self.generatedLinesSettings = []

        view.draw()
        self.consoleController = parent.getControllerRefferenceOf("console")
        self.consoleController.printToRightConsole("test print")


    def genLineSettings(self):
        if (len(self.generatedLinesSettings) > 0): return self.generatedLinesSettings
        if self.loadCachedLineSettings(defaults.cachedSettingsPath):
            print("loading from cache")
            pass
        else:
            for i in range(defaults.initialNrOfLineSettings):
                lineSetting = setupPage.lineSettings("Line " + str(i), defaults.predefinedColors[i], True, defaults.axisOptions[0], i)
                self.generatedLinesSettings.append(lineSetting)

        return self.generatedLinesSettings


    def addLine(self): #dodaj line do te cifre ali jih samo make visible
        if len(self.generatedLinesSettings)==defaults.maxNrOfLines:
            self.consoleController.printToRightConsole("You have reached maximum number of lines: " + str(defaults.maxNrOfLines))
            return
        hiddenLinesExist = False
        for line in self.generatedLinesSettings:
            if not line.visibility and not hiddenLinesExist:
                #print("setting visibilit to True")
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
        for index, line in enumerate(reversed(self.generatedLinesSettings)):
            #print(line.id, line.visibility)
            if not line.visibility:
                hiddenLinesExist = True
                if self.generatedLinesSettings[line.id-1].visibility == True:
                    self.generatedLinesSettings[line.id-1].visibility = False
                    break
   
        if not hiddenLinesExist:
            self.generatedLinesSettings[-1].visibility = False
        self.view.draw()
        


    def loadCachedLineSettings(self, path): #nalož iz cacheta - pogruntej json
        return None


    def openFile(self):
        print("implement open file")
        pass