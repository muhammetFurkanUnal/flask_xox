import sys
from ..config import *
from .xoxEngine import Game
from .exceptions import *
import json

game = Game()

# game loop
while True:
    
    # try:
    #     game.move(row, column)
    # except IllegalMoveError as e:
    #     comModule.output(str(e))
    #     continue
    
    # check if game is finished 
    code = game.log["winner"]
    if code == 0:  # code for game continues
        # comModule.output(json.dumps(game.log))
        continue
    elif code == 1:  # code for X
        # print("X wins!")
        # comModule.output(json.dumps(game.log))
        break
    elif code == 2:  # code for Y
        # print("O wins!")
        # comModule.output(json.dumps(game.log))
        break
    elif code == -1:  # code for draw
        # print("Draw!")
        # comModule.output(json.dumps(game.log))
        break
