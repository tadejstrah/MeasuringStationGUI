import defaults
import setupPage.lineSettings


class setupController():
    def __init__(self, view, parent):
        self.view = view
        view.controller = self
        view.draw()
        consoleController = parent.getControllerRefferenceOf("console")
        consoleController.printToRightConsole("test print")


    def genLineSettings(self):
        generatedLinesSettings = []
        if self.loadCachedLineSettings(defaults.cachedSettingsPath):
            print("loading from cache")
            pass
        else:
            for i in range(defaults.initialNrOfLineSettings):
                lineSetting = setupPage.lineSettings("name", "color", "visibility", "axis")
                generatedLinesSettings.append(lineSetting)
            

        return generatedLinesSettings

    def addLine(self): #dodaj line do te cifre ali jih samo make visible
        return []

    def removeLine(self): #removaj line/ make them not visible
        return []

    def loadCachedLineSettings(self, path): #nalož iz cacheta - pogruntej json
        return None