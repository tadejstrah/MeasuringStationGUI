import json

class graphLine():
    def __init__(self, id, name, axis, color):
        self.id = id
        self.name = name
        self.axis = axis
        self.color = color
        self.YData = []
        self.line = None
    
    def stringify(self):
        return [self.id, self.name, self.axis, self.color, self.YData]