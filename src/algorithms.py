import random
import math

X_player = 'X',
O_player = 'O',
emptyCell = '-'

scores = {
    'X': 10,
    'O': -10,
    '-': 0
}

def simplePick(board):
    emptyCells = []
    for i in range (len(board)):
        if (board[i] == emptyCell):
            emptyCells.append(i)
    
    return random.choice(emptyCells)


def findBestMove(board):
    bestScore = -math.inf
    bestMove = -1

    for cellIndex in range(len(board)):
        if(board[cellIndex] == emptyCell):
            board[cellIndex] = X_player
            score = minimax(board, 1, True)
            
            board[cellIndex] = emptyCell

            if(score > bestScore):
                bestScore = score
                print(cellIndex)
                bestMove = cellIndex
    
    return bestMove

def minimax(board, depth, isMax):
    winner = getWinner(board)

    if(winner != None and winner != '-'):
        return scores[winner]
    
    if(isMax):
        bestScore = -math.inf
        
        for cellIndex in range(len(board)):
            if(board[cellIndex] == emptyCell):
                board[cellIndex] = X_player
                score = minimax(board, depth + 1, False)
                board[cellIndex] = emptyCell
                
                bestScore = max(score, bestScore)
        return (bestScore - depth)
    
    else:
        bestScore = -math.inf

        for cellIndex in range(len(board)):
            if(board[cellIndex] == emptyCell):
                board[cellIndex] = O_player
                score = minimax(board, depth + 1, True)
                board[cellIndex] = emptyCell
            
                bestScore = max(score, bestScore)
        return (bestScore - depth)

def getWinner(board):
    lines = [[0, 1, 2],[3, 4, 5],[6, 7, 8],[0, 3, 6],[1, 4, 7],[2, 5, 8],[0, 4, 8],[2, 4, 6]]

    for i in range(len(lines)):
        [a, b, c] = lines[i]

        if(board[a] and board[a] == board[b] and board[a] == board[c]):
            return board[a]
    
    return None