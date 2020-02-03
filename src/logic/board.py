from logic.cell import Cell

class Board:
    numberOfCells = 9


    def __init__(self):
        self.cells = []
        for _ in range(self.numberOfCells):
            self.cells.append(Cell())

    
    def getCells(self):
        returnList = []

        for cell in self.cells:
            returnList.append(cell.getValue())
        
        return returnList

    def getCell(self, index):
        return self.cells[index].getValue()

    def setCellValue(self, index, value):
        try:
            self.cells[index].setValue(value)
        except Exception:
            raise Exception('Index should be positive and  <= ' + str(self.numberOfCells))