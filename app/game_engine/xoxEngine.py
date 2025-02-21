# errors must be catched in game loop
from .exceptions import IllegalMoveError

class Game:
    move_number = -1
    turn_X = True  # X starts the game
    
    # use codes for checks and operations
    X_code = 1
    O_code = 2
    
    # use representative codes when printing and no where else
    X_repr = "X"
    O_repr = "O"
    
    # move_number, X or O (1 or 2), axis0, axis1 
    # move_list = []
    
    
    def __init__(self):
        
        self.flat_board = [0,0,0,0,0,0,0,0,0]
        self.log = {
            "move_number":self.move_number,
            # "move_list":move_list,
            "turn": self.X_code,
            "winner":0,
            "flat_board": self.flat_board
        }
        
        self.board = [[0,0,0],
                [0,0,0],
                [0,0,0]]
    
    
    def printBoard(self):
        
        """
        foreach in all the board matrix 
        print X_repr if X_code
        print O_repr if O_code
        print 0 if no piece
        """
        board = []

        
        for i in self.board:
            for j in i:
                piece = None
                if j == self.X_code:
                    piece = self.X_repr
                elif j == self.O_code:
                    piece = self.O_repr
                else:
                    piece = "0"
                    
                board.append(piece)
            
        boardstr = f"""
    0  1  2
  ----------
0 | {board[0]}  {board[1]}  {board[2]}
1 | {board[3]}  {board[4]}  {board[5]}
2 | {board[6]}  {board[7]}  {board[8]}      
"""
        print(boardstr)
        
        
    def getFlatBoard(self):
        return [j for i in self.board for j in i]
            

    def putX(self, axis0, axis1):
        # if position is out of range
        if axis0 > 2 or axis1 > 2 or axis0 < 0 or axis1 < 0:
            raise IllegalMoveError(f"Position ({axis0}, {axis1}) is out of boundary.")
        
        # if position is not empty
        if self.board[axis0][axis1] != 0:
            raise IllegalMoveError(f"Trying to put position ({axis0}, {axis1}) {self.X_repr} but position is not empty.")
        
        self.board[axis0][axis1] = self.X_code
        
        
        
    def putO(self, axis0, axis1):
        # if position is out of range
        if axis0 > 2 or axis1 > 2 or axis0 < 0 or axis1 < 0:
            raise IllegalMoveError(f"Position ({axis0}, {axis1}) is out of boundary.")
        
        # if position is not empty
        if self.board[axis0][axis1] != 0:
            self.printBoard()
            raise IllegalMoveError(f"Trying to put position ({axis0}, {axis1}) {self.O_repr} but position is not empty.")
        
        self.board[axis0][axis1] = self.O_code
        


    def move(self, axis0, axis1):
        
        """
        utilizes putX() and putO() to automatically understand who's turn 
        and if game finishes after the move 
        """
        
        player = None
        if self.turn_X:
            player = self.X_code
            self.putX(axis0, axis1)
            self.turn_X = False
            
        else:
            player = self.O_code
            self.putO(axis0, axis1)
            self.turn_X = True
            
        winner = self.checkWin()
        self.move_number += 1
        # self.move_list.append([self.move_number, player, axis0, axis1])
        self.updateLog(self.move_number, winner)
        
        
    def updateLog(self, move_number, winner):
        self.log["winner"] = winner
        self.log["move_number"] = move_number
        # self.log["move_list"] = move_list
        self.log["flat_board"] = self.getFlatBoard()
        self.log["turn"] = self.X_code if self.turn_X else self.O_code
        
        # no need to update move_list because it is already the pointer of 
        # move list list object, only updating list is enough
        
        
    
    
    def checkWin(self):
        if self.checkWin_forPlayer(1): # X
            return 1
        elif self.checkWin_forPlayer(2): # O
            return 2
        elif self.checkDraw():
            return -1
        else:
            return 0  # game continues
        
    
    # player is 1 or 2, X_code or O_code
    def checkWin_forPlayer(self, player):
        # check vertical
        for i in range(3):
            if self.board[i][0] == player and self.board[i][1] == player and self.board[i][2] == player:
                return True
            
        # check horizontal
        for i in range(3):
            if self.board[0][i] == player and self.board[1][i] == player and self.board[2][i] == player:
                return True
            
        # check diagonals
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            return True
        
        if self.board[2][0] == player and self.board[1][1] == player and self.board[0][2] == player:
            return True
        
        
        # if no condition works
        return False
    
    
    def checkDraw(self):
        for i in self.board:
            for j in i:
                if j == 0:
                    return False
                
        # if could not find empty place
        return True