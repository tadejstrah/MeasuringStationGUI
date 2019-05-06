import csv
from tkinter import filedialog
import io

class dataManager():
    def __init__(self,dataArrays):
        self.dataToSave = dataArrays


    def saveToFile(self):

        out = io.StringIO()
        
        writer = csv.writer(out, dialect="excel")
        writer.writerow(["First line declares the number of lines to draw, first data line represents time/XAxis and the following lines contain the YAxis data"])
        writer.writerow(str(len(self.dataToSave)))
        writer.writerow(self.dataToSave[0].XData)
        for x in self.dataToSave:
            writer.writerow(x.YData)
        
        outFile = filedialog.asksaveasfile(mode="w",defaultextension=".txt")
        outFile.write(out.getvalue())
        outFile.close()
