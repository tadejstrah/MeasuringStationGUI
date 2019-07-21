import csv
from tkinter import filedialog
import io
import easygui
from datetime import datetime
import GraphLine

class dataManager():
    def __init__(self,dataArrays):
        self.dataToSave = dataArrays

        
    def saveToFile(self):
        #print(datetime.now())
        filename = easygui.filesavebox(default=datetime.now().strftime("%Y-%m-%d_%H-%M")+".txt", filetypes=["*.txt"])
        print(filename)

        if not filename: return

        with open(filename, mode="w") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=";")
            csv_writer.writerow(["First row declares the number of lines, next line represents time/XAxis and the following lines contain parameters and YAxis data of lines"])
            csv_writer.writerow(["Nr. of lines:",str(len(self.dataToSave))])
            neki = self.dataToSave[0].XData
            neki.insert(0,"XData:")
            csv_writer.writerow(neki)
            csv_writer.writerow([])

            for y,x in enumerate(self.dataToSave):
                csv_writer.writerow(["Line "+str(y+1),x._color, x._axis, x._name])
                csv_writer.writerow(x.YData)


    def openFile(self):
        openFile_Name = easygui.fileopenbox()

        with open(openFile_Name) as csv_file:
            temp_xData = []
            csv_reader = csv.reader(csv_file, delimiter = ";")
            line_count = 0
            temp_line_count = 0
            temp_line = GraphLine.GraphLine("","","")
            inputData = []

            for row in csv_reader:
                if len(row) > 0:
                    if line_count == temp_line_count+2 and line_count > 2:
                        #print(line_count)
                        temp_line.YData = row
                        temp_line.YData = list(map(float, temp_line.YData))
                        inputData.append(temp_line)
                        #print(row)
                    if "XData" in row[0]:
                        temp_xData = row[1:]
                        temp_xData = list(map(float, temp_xData))
                    if "Line " in row[0] and line_count is not 0 and line_count is not 2:
                        #print(row)
                        #print(line_count)
                        temp_line = GraphLine.GraphLine(row[1], row[2], row[3])
                        temp_line.XData = temp_xData
                        temp_line_count = line_count

                line_count += 1
            #print(len(inputData))
            #print(inputData[0].YData)
        for x in inputData:
            pass
            #print(x.XData)
            #print(x.YData)
            #print()
            #print(x)
            #print(x.XData)
            #print(x.YData)
        return inputData

    def saveToFile2(self):

        out = io.StringIO()
        
        writer = csv.writer(out, dialect="excel")
        writer.writerow(["First line declares the number of lines to draw, first data line represents time/XAxis and the following lines contain the YAxis data"])

        for x in self.dataToSave:
            writer.writerow(x.YData)
        
        outFile = filedialog.asksaveasfile(mode="w",defaultextension=".txt")
        outFile.write(out.getvalue())
        outFile.close()

