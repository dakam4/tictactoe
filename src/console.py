from logic.game import Game

def printBoard(board):
    print()
    print('-' * 13)
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('-' * 13)
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('-' * 13)
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('-' * 13)
    print()


game = Game()
index = int(input('Player ' + game.getNextPlayer() + ' (Move from 0 to 8 inclusive): '))

while(len(game.winner) == 0 and index != -1):
    if index in range(0, 9):
        game.makeMove(index)
    else:
        print('Error!')
        print('The move should be between 0 and 8 inclusive.')
    
    printBoard(game.getBoardList())

    index = int(input('Player ' + game.getNextPlayer() + ' (Move from 0 to 8 inclusive): '))


printBoard(game.getBoardList())
print()
print('-----------GAME-OVER---------------')
print()
if(game.getWinner() == 'X' or game.getWinner() == 'O'):
    print('THE WINNER IS :   ' + game.getWinner())
elif(game.getWinner() == 'N'):
    print('DRAW')
else:
    print('GAME INTERRUPTED!')
print()
print('-----------------------------------')
print()