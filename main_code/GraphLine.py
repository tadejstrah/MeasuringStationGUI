
class GraphLine():
    def __init__(self, color, axis,name):
        self.XData = [0,0]
        self.YData = [0,0]
        self._color = color
        self._axis = axis
        self.prevX = 0
        self._name = name
