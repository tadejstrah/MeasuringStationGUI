

class graphController():
    def __init__(self, view, parent):
        self.view = view
        view.controller = self
        view.draw()
