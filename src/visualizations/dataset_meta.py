import numpy as np
import random
'''
    Collect metadata of datasets
'''
class metadata:
    columns = []
    columnTypes = []
    columnCount = 0
    rowCount = 0
    delimiter = ""
    chosenColumns = None
    #numericColumns = None

    def collect_metadata(self, file):
        print(file)
        temp = file.split('.')
        extension = temp[len(temp)-1]
        if extension == "tab":
            self.delimiter= '\t'
        if extension == "csv":
            self.delimiter = ','
        else:
            Exception("File Error: Not recognized file extension.")

        with open(file, 'r') as file:
            columns = file.readline().split(self.delimiter)

            columnCount = len(columns)
            self.columnCount = columnCount

            columns[columnCount-1] = columns[columnCount-1].strip('\n')           
            self.columns = columns

            if self.delimiter == '\t': # lmao
                typeSample = file.readline()
                typeSample = file.readline()
            typeSample = file.readline()

            file.seek(0, 0)
            rowCount = len(file.readlines())
            self.rowCount = rowCount

            columnTypes = []
            typeSample = typeSample.split(self.delimiter)
            for cell in typeSample:
                if cell.replace('.', '', 1).isdigit():
                    columnTypes.append('number')
                elif cell == '':
                    columnTypes.append('null')
                else:
                    #print("STRING:", cell)
                    columnTypes.append('string')
            self.columnTypes = columnTypes
    
    def get_numeric_columns(self):
        usedColumnIds = []
        usedColumns = []
        usedColumnCount = 0
        for i, t in enumerate(self.columnTypes):
            if t.__eq__('number'):
                usedColumnIds.append(i)
                usedColumns.append(self.columns[i])
                usedColumnCount += 1
        return usedColumnCount, usedColumns, usedColumnIds

