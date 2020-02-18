from logic.game import Game
import algorithms


options = [1, 2, 3]

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
index = 0

print('-' * 20)
print('Available opions:')
print('1 - Simple')
print('2 - Impossible')
print('3 - Play against a friend')
print('-' * 20)
print()
playingOption = -1

while(not(playingOption in options)):
    if(not(playingOption in options) and playingOption != -1):
        print('Invalid input.')
    playingOption = int(input('Select an option: [1,2,3]: '))

while(len(game.winner) == 0 and index != -1):
    index = int(input('Player ' + game.getNextPlayer() + ' (Move range [0,8]): '))

    if index in range(0, 9):
        game.makeMove(index)
        if(playingOption == 1 and len(game.winner) == 0):
            game.makeMove(algorithms.simplePick(game.getBoardList()))
        if(playingOption == 2 and len(game.winner) == 0):
            game.makeMove(algorithms.findBestMove(game.getBoardList()))
    else:
        print('Error!')
        print('The move should be between 0 and 8 inclusive.')
    
    printBoard(game.getBoardList())

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