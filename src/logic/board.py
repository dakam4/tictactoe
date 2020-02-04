from logic.cell import Cell

class Board:
    numberOfCells = 9
    minimumIndex = 0

    def __init__(self):
        self.cells = []
        for _ in range(self.numberOfCells):
            self.cells.append(Cell())

    """This function transforms the object of type Board to
        its minimized version
    
    Returns:
        list -- simple version of the board
    """
    def getSimplifiedBoard(self):
        returnList = []

        for cell in self.cells:
            returnList.append(cell.getValue())
        
        return returnList

    def getCell(self, index):
        self.validateIndex(index)
        
        return self.cells[index].getValue()

    def setCellValue(self, index, value):
        self.validateIndex(index)

        try:
            self.cells[index].setValue(value)
        except Exception as e:
            raise e

    def validateIndex(self, index):
        if(not(index in range(self.minimumIndex, self.numberOfCells))):
            raise Exception('The index should be in the range [' + str(self.minimumIndex) + ',' + str(self.numberOfCells) + '[' )