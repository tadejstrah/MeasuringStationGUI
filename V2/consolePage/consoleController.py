

class consoleController():
    def __init__(self, view, parent):
        self.view = view
        view.controller = self
        view.draw()
    
    def printToLeftConsole(self,string):
        self.view.printToLeftConsole(string)

    def printToRightConsole(self,string):
        self.view.printToRightConsole(string)