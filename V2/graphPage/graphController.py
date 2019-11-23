import graphPage.graphLine

class graphController():
    def __init__(self, view, parent):
        self.view = view
        view.controller = self

        self.rawData = []
        self.data = []

        self.parent = parent

        #view.draw()
        

    def setData(self, data):
        self.rawData = data
        self.view.draw()
        #print(data)

    def getData(self):
        if not self.rawData: return []
        if len(self.data) > 0: return self.data
        for index, value in enumerate(self.rawData[0]):
            graphLine = graphPage.graphLine(index, self.rawData[1][index],self.rawData[2][index], self.rawData[3][index] )  #id, name, axis, color
            self.data.append(graphLine)
        return self.data

    def goToSetupPage(self):
        self.parent.showPage("setup", self)