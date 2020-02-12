from logic.board import Board


class Game:
    numberOfStates = 10
    minimumState = 0

    def __init__(self):
        self.board = Board()
        self.statesOfBoard = []
        self.statesOfBoard.append(self.board)
        self.winner = ''
        self.nextPlayer = 'X'

    def getWinner(self):
        return self.winner
    
    def setBoard(self, board):
        self.board = board

    def getNextPlayer(self):
        return self.nextPlayer

    def getBoardList(self):
        return self.board.getSimplifiedBoard()

    def makeMove(self, cellIndex):
        self.board.setCellValue(cellIndex, self.nextPlayer)
        self.statesOfBoard.append(self.board)
        self.togglePlayer()
        return self.hasResult()

    def isEndOfGame(self):
        if(len(self.statesOfBoard) == self.numberOfStates - 1):
            self.winner = 'N'
            return True
        return False
    
    def hasResult(self):
        lines = [[0, 1, 2],[3, 4, 5],[6, 7, 8],[0, 3, 6],[1, 4, 7],[2, 5, 8],[0, 4, 8],[2, 4, 6]]

        for i in range(len(lines)):
            [a, b, c] = lines[i]

            if(self.board.getCell(a) and self.board.getCell(a) == self.board.getCell(b) and
            self.board.getCell(a) == self.board.getCell(c)):
                self.winner = self.board.getCell(a) if self.board.getCell(a) != '-' else ''
                return True
        
        return self.isEndOfGame()

    def togglePlayer(self):
        if(self.nextPlayer == 'X'):
            self.nextPlayer = 'O'
        else:
            self.nextPlayer = 'X'
    
    def returnToState(self, number):
        if(number > len(self.numberOfStates) or number < self.minimumState):
            raise Exception('Invalid state. Shoud be in range [' + str(self.minimumState) + ',' + str(self.numberOfStates) + '[')

        self.board = self.statesOfBoard[number]