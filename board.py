# author: Rushil Nagpal
# date: 27th April, 2023
# file: tictac.py a Python program that implements a tic-tac-toe game
# input: user responses (strings)
# output: interactive text messages and a tic-tac-toe board
class Board:
    def __init__(self):
    # board is a list of cells that are represented
    # by strings (" ", "O", and "X")
    # initially it is made of empty cells represented
    # by " " strings
        self.sign = " "
        self.size = 3
        self.board = list(self.sign * self.size**2)
        # the winner's sign O or X
        self.winner = ""
    def get_size(self):
        return self.size
    # optional, return the board size (an instance size)            #for example 3 
    def get_winner(self):
        return self.sign                                            
    # return the winner's sign O or X (an instance winner)
    def set(self, cell, sign):
    # mark the cell on the board with the sign X or O
        self.cell = cell
        self.sign = sign
        valid_choices = ["A1","B1","C1","A2","B2","C2","A3","B3","C3"]
        index = valid_choices.index(cell)
        self.board[index] = sign
    def isempty(self, cell):
        valid_choices = ["A1","B1","C1","A2","B2","C2","A3","B3","C3"]
        index = valid_choices.index(cell)
        if self.board[index] == " ":
            return True
        else:
            return False

    # return True if the cell is empty (not marked with X or O)
    def isdone(self):
        done = False
        if self.board[0] == self.board[1] == self.board[2] != " ":
            done = True                                                             #checking conditions if all the positions are
            self.sign = self.board[0]                                                 # occupied in the board.
        elif self.board[3] == self.board[4] == self.board[5] != " ":
            done = True
            self.sign = self.board[3]
        elif self.board[6] == self.board[7] == self.board[8] != " ":
            done = True
            self.sign = self.board[6]
        elif self.board[0] == self.board[3] == self.board[6] != " ":
            done = True
            self.sign = self.board[0]
        elif self.board[1] == self.board[4] == self.board[7] != " ":
            done = True
            self.sign = self.board[1]
        elif self.board[2] == self.board[5] == self.board[8] != " ":
            done = True
            self.sign = self.board[2]
        elif self.board[0] == self.board[4] == self.board[8] != " ":
            done = True
            self.sign = self.board[0]
        elif self.board[2] == self.board[4] == self.board[6] != " ":
            done = True
            self.sign = self.board[2]
        else:
            if " " not in self.board:
                done = True
                self.sign = " "
        

    # check all game terminating conditions, if one of them is present,
    #assign the var done to True
    # depending on conditions assign the instance var winner to O or X
        return done
    def show(self):
    # draw the board                                                                       
    # need to complete the code
        print("   A   B   C")
        print(f' +---+---+---+\n1| {self.board[0]} | {self.board[1]} | {self.board[2]} |')
        print(f' +---+---+---+\n2| {self.board[3]} | {self.board[4]} | {self.board[5]} |')
        print(f' +---+---+---+\n3| {self.board[6]} | {self.board[7]} | {self.board[8]} |')
        print(" +---+---+---+\n")