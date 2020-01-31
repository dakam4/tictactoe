from logic.game import Game


game = Game()
index = int(input('Player ' + game.getNextPlayer() + ' (Move from 0 to 8 inclusive): '))

while(len(game.winner) == 0 and index != -1):
    if index in range(0, 9):
        game.makeMove(index)
    else:
        print('Error!')
        print('The move should be between 0 and 8 inclusive.')
    index = int(input('Player ' + game.getNextPlayer() + ' (Move from 0 to 8 inclusive): '))



print()
print('-----------GAME-OVER---------------')
print()
if(game.getWinner() != 'N'):
    print('THE WINNER IS :   ' + game.getWinner())
else:
    print('DRAW')
print()
print('-----------------------------------')
print()