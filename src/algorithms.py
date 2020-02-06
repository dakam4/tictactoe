import random


def simplePick(board):
    emptyCells = []
    for i in range (len(board)):
        if (board[i] == '-'):
            emptyCells.append(i)
    
    return random.choice(emptyCells)