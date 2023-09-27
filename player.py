
class Player:
      def __init__(self, name, sign):
            self.name = name # player's name
            self.sign = sign # player's sign O or X
      def get_sign(self):
            return self.sign
      # return an instance sign
      def get_name(self):
            return self.name
      # return an instance name
      def choose(self, board):
      # prompt the user to choose a cell
      # if the user enters a valid string and the cell on the board is empty,
      #update the board
      # otherwise print a message that the input is wrong and rewrite the
      #prompt
      # use the methods board.isempty(cell), and board.set(cell, sign)
            valid_choices = ["A1","B1","C1","A2","B2","C2","A3","B3","C3"]
            while True:
                        if " " in board.board:
                              cell = input(f'\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]:\n').upper()
                              if cell in valid_choices :
                                    if board.isempty(cell):
                                          board.set(cell, self.sign)
                                          break
                                    else:
                                          print("You did not choose correctly.")
                        else:
                               break
from random import choice
class AI(Player):
      def __init__(self,name,sign,board):
            Player.__init__(self,name,sign)                                 
            self.board = board.board
      def choose(self, board):
            valid_choices = ["A1","B1","C1","A2","B2","C2","A3","B3","C3"]
            ty = []
            print(f'\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]:')
            while True:
                        if " " in self.board:
                              if valid_choices != []:
                                     cell = choice(valid_choices)                         # choosing random cell from
                                     if board.isempty(cell):                              #list of choices and editing the list
                                          board.set(cell, self.sign)                      #so that it doesn't repeat its move.
                                          print(cell)
                                          ty.append(cell)
                                          valid_choices.remove(cell)
                                          break
                              else:
                                     break
                        else:
                               break

class MiniMax(AI):
      def __init__(self,name,sign,board):
              AI.__init__(self,name,sign,board)
      def choose(self, board):
            if self.sign == "O":
                   self.opponent_sign = "X"
            else:
                   self.opponent_sign = "O"
            print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
            cell =  MiniMax.minimax(self, board, True, True)                              #calling MiniMax first time when both conditions
            print(cell)                                                                   # are true.
            board.set(cell,self.sign)

      def minimax(self, board, self_player, start):
      # check the base conditions
            if board.isdone():
                  # self is a winner
                  if board.get_winner() == self.sign:
                        return 1
                  # is a tie
                  elif board.get_winner() == " ":
                        return 0
                  # self is a looser (opponent is a winner)
                  else:
                        return -1
            
            maxscore = -10 # (any small number < -1 or float('-inf'))
            minscore = 10 #(any big number > 1 or float('inf'))
            move = 0
            for lol in range(len(self.board)):                                       # make a move (choose a cell) recursively                                   
                        if self.board[lol] == " ":                            # make a move (choose a cell) recursively
                              valid_choices = ["A1","B1","C1","A2","B2","C2","A3","B3","C3"] 
                              moves = valid_choices[lol]
                  # call minimax recursively
                              if self_player:
                                    board.set(moves, self.sign)
                                    score = MiniMax.minimax(self, board, False, False)                #when both conditions are false
                                    if score > maxscore:                                             #maximising the score for the move
                                          maxscore = score
                                          move = valid_choices[lol]
                  
                              else:         
                                    board.set(moves,self.opponent_sign)
                                    score = MiniMax.minimax(self, board, True,False)               #self_player is True and start is False
                                    if score < minscore:
                                          minscore = score                                         #minimising the score for opponent
                                          move = valid_choices[lol]
                              board.set(moves," ")                                              #setting the move in recursion to " "
            if start:
                  return move                                                                       
            elif self_player:
                  return maxscore
            else:
                  return minscore
class SmartAI(AI):
      def __init__(self,name,sign,board):
              AI.__init__(self,name,sign,board)
      def self_win(self,board):
            if self.sign == "O":
                  self.opponent_sign = "X"
            else:
                  self.opponent_sign = "O"
            valid_choices = ["A1","B1","C1","A2","B2","C2","A3","B3","C3"]
            if self.board[0] == self.board[1] == self.sign and self.board[2] == " ":
                  board.set(valid_choices[2],self.sign)                                               #checking all possible conditions
                  print(valid_choices[2])                                                             #for self_win
                  return True
            elif self.board[4] == self.board[6] == self.sign and self.board[2] == " ":
                  board.set(valid_choices[2],self.sign)
                  print(valid_choices[2])
                  return True
            elif self.board[4] == self.board[2] == self.sign and self.board[6] == " ":
                  board.set(valid_choices[6],self.sign)
                  print(valid_choices[6])
                  return True
            elif self.board[6] == self.board[2] == self.sign and self.board[4] == " ":
                  board.set(valid_choices[4],self.sign)
                  print(valid_choices[4])
                  return True
            elif self.board[0] == self.board[4] == self.sign and self.board[8] == " ":
                  board.set(valid_choices[8],self.sign)
                  print(valid_choices[8])
                  return True
            elif self.board[4] == self.board[8] == self.sign and self.board[0] == " ":
                  board.set(valid_choices[0],self.sign)
                  print(valid_choices[0])
                  return True
            elif self.board[0] == self.board[8] == self.sign and self.board[4] == " ":
                  board.set(valid_choices[4],self.sign)
                  print(valid_choices[4])
                  return True
            elif self.board[1] == self.board[2] == self.sign and self.board[0] == " ":
                  board.set(valid_choices[0],self.sign)
                  print(valid_choices[0])
                  return True
            elif self.board[0] == self.board[2] == self.sign and self.board[1] == " ":
                  board.set(valid_choices[1],self.sign)
                  print(valid_choices[1])
                  return True
            elif self.board[3] == self.board[4] == self.sign and self.board[5] == " ":
                  board.set(valid_choices[5],self.sign)
                  print(valid_choices[5])
                  return True
            elif self.board[3] == self.board[5] == self.sign and self.board[4] == " ":
                  board.set(valid_choices[4],self.sign)
                  print(valid_choices[4])
                  return True
            elif self.board[5] == self.board[4] == self.sign and self.board[3] == " ":
                  board.set(valid_choices[3],self.sign)
                  print(valid_choices[3])
                  return True
            elif self.board[6] == self.board[7] == self.sign and self.board[8] == " ":
                  board.set(valid_choices[8],self.sign)
                  print(valid_choices[8])
                  return True

            elif self.board[7] == self.board[8] == self.sign and self.board[6] == " ":
                  board.set(valid_choices[6],self.sign)
                  print(valid_choices[6])
                  return True
            elif self.board[6] == self.board[8] == self.sign and self.board[7] == " ":
                  board.set(valid_choices[7],self.sign)
                  print(valid_choices[7])
                  return True
            elif self.board[2] == self.board[8] == self.sign and self.board[5] == " ":
                  board.set(valid_choices[5],self.sign)
                  print(valid_choices[5])
                  return True
            elif self.board[5] == self.board[8] == self.sign and self.board[2] == " ":
                  board.set(valid_choices[2],self.sign)
                  print(valid_choices[2])
                  return True
            elif self.board[2] == self.board[5] == self.sign and self.board[8] == " ":
                  board.set(valid_choices[8],self.sign)
                  print(valid_choices[8])
                  return True
            elif self.board[3] == self.board[6] == self.sign and self.board[0] == " ":
                  board.set(valid_choices[0],self.sign)
                  print(valid_choices[0])
                  return True
            elif self.board[0] == self.board[6] == self.sign and self.board[3] == " ":
                  board.set(valid_choices[3],self.sign)
                  print(valid_choices[3])
                  return True
            elif self.board[0] == self.board[3] == self.sign and self.board[6] == " ":
                  board.set(valid_choices[6],self.sign)
                  print(valid_choices[6])
                  return True
            elif self.board[1] == self.board[4] == self.sign and self.board[7] == " ":
                  board.set(valid_choices[7],self.sign)
                  print(valid_choices[7])
                  return True
            elif self.board[4] == self.board[7] == self.sign and self.board[1] == " ":
                  board.set(valid_choices[1],self.sign)
                  print(valid_choices[1])
                  return True
            elif self.board[1] == self.board[4] == self.sign and self.board[7] == " ":
                  board.set(valid_choices[7],self.sign)
                  print(valid_choices[7])
                  return True
      def check_opponent_win(self,board):
            if self.sign == "O":
                  self.opponent_sign = "X"
            else:
                  self.opponent_sign = "O"
      
            valid_choices = ["A1","B1","C1","A2","B2","C2","A3","B3","C3"]
            if self.board[0] == self.board[1] == self.opponent_sign and self.board[2] == " ":              #checking all possible condtions
                  board.set(valid_choices[2],self.sign)                                                    #for opponent_win 
                  print(valid_choices[2])                                                                               
                  return True
            elif self.board[4] == self.board[6] == self.opponent_sign and self.board[2] == " ":
                  board.set(valid_choices[2],self.sign)
                  print(valid_choices[2])
                  return True
            elif self.board[4] == self.board[2] == self.opponent_sign and self.board[6] == " ":
                  board.set(valid_choices[6],self.sign)
                  print(valid_choices[6])
                  return True
            elif self.board[6] == self.board[2] == self.opponent_sign and self.board[4] == " ":
                  board.set(valid_choices[4],self.sign)
                  print(valid_choices[4])
                  return True
            elif self.board[0] == self.board[4] == self.opponent_sign and self.board[8] == " ":
                  board.set(valid_choices[8],self.sign)
                  print(valid_choices[8])
                  return True
            elif self.board[4] == self.board[8] == self.opponent_sign and self.board[0] == " ":
                  board.set(valid_choices[0],self.sign)
                  print(valid_choices[0])
                  return True
            elif self.board[0] == self.board[8] == self.opponent_sign and self.board[4] == " ":
                  board.set(valid_choices[4],self.sign)
                  print(valid_choices[4])
                  return True
            elif self.board[1] == self.board[2] == self.opponent_sign and self.board[0] == " ":
                  board.set(valid_choices[0],self.sign)
                  print(valid_choices[0])
                  return True
            elif self.board[0] == self.board[2] == self.opponent_sign and self.board[1] == " ":
                  board.set(valid_choices[1],self.sign)
                  print(valid_choices[1])
                  return True
            elif self.board[3] == self.board[4] == self.opponent_sign and self.board[5] == " ":
                  board.set(valid_choices[5],self.sign)
                  print(valid_choices[5])
                  return True
            elif self.board[3] == self.board[5] == self.opponent_sign and self.board[4] == " ":
                  board.set(valid_choices[4],self.sign)
                  print(valid_choices[4])
                  return True
            elif self.board[5] == self.board[4] == self.opponent_sign and self.board[3] == " ":
                  board.set(valid_choices[3],self.sign)
                  print(valid_choices[3])
                  return True
            elif self.board[6] == self.board[7] == self.opponent_sign and self.board[8] == " ":
                  board.set(valid_choices[8],self.sign)
                  print(valid_choices[8])
                  return True

            elif self.board[7] == self.board[8] == self.opponent_sign and self.board[6] == " ":
                  board.set(valid_choices[6],self.sign)
                  print(valid_choices[6])
                  return True
            elif self.board[6] == self.board[8] == self.opponent_sign and self.board[7] == " ":
                  board.set(valid_choices[7],self.sign)
                  print(valid_choices[7])
                  return True
            elif self.board[2] == self.board[8] == self.opponent_sign and self.board[5] == " ":
                  board.set(valid_choices[5],self.sign)
                  print(valid_choices[5])
                  return True
            elif self.board[5] == self.board[8] == self.opponent_sign and self.board[2] == " ":
                  board.set(valid_choices[2],self.sign)
                  print(valid_choices[2])
                  return True
            elif self.board[2] == self.board[5] == self.opponent_sign and self.board[8] == " ":
                  board.set(valid_choices[8],self.sign)
                  print(valid_choices[8])
                  return True
            elif self.board[3] == self.board[6] == self.opponent_sign and self.board[0] == " ":
                  board.set(valid_choices[0],self.sign)
                  print(valid_choices[0])
                  return True
            elif self.board[0] == self.board[6] == self.opponent_sign and self.board[3] == " ":
                  board.set(valid_choices[3],self.sign)
                  print(valid_choices[3])
                  return True
            elif self.board[0] == self.board[3] == self.opponent_sign and self.board[6] == " ":
                  board.set(valid_choices[6],self.sign)
                  print(valid_choices[6])
                  return True
            elif self.board[1] == self.board[4] == self.opponent_sign and self.board[7] == " ":
                  board.set(valid_choices[7],self.sign)
                  print(valid_choices[7])
                  return True
            elif self.board[4] == self.board[7] == self.opponent_sign and self.board[1] == " ":
                  board.set(valid_choices[1],self.sign)
                  print(valid_choices[1])
                  return True
            elif self.board[1] == self.board[4] == self.opponent_sign and self.board[7] == " ":
                  board.set(valid_choices[7],self.sign)
                  print(valid_choices[7])
                  return True
                  
      def choose(self,board):
            if self.sign == "O":                                                                
                   self.opponent_sign = "X"
            else:
                  self.opponent_sign = "O"
            valid_choices = ["A1","B1","C1","A2","B2","C2","A3","B3","C3"]
            while True:
                  print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")                     #giving some set of moves
                  if self.sign == "X":                                                                #to make SmartAI win
                        if self.board[0] == " ":
                              board.set(valid_choices[0],self.sign)
                              print(valid_choices[0])                                                 #calling all functions 
                              break     
                  elif self.self_win(board):
                        break
                  elif self.check_opponent_win(board):
                        break                                                              
                  elif self.sign == "X":
                        if self.board[2] == " ":
                              board.set(valid_choices[2],self.sign)
                              print(valid_choices[2])
                              break  
                  elif self.self_win(board):
                        break
                  elif self.check_opponent_win(board):
                        break
                  elif self.sign == "X":
                        if self.board[6] == " ":
                              board.set(valid_choices[6],self.sign)
                              print(valid_choices[6])
                              break  
                  elif self.self_win(board):
                        break
                  elif self.check_opponent_win(board):
                        break
                  elif self.sign == "X":
                        if self.board[8] == " ":
                              board.set(valid_choices[8],self.sign)
                              print(valid_choices[8])
                              break  
                  elif self.self_win(board):
                        break
                  elif self.check_opponent_win(board):
                        break
                  elif self.sign == "X":
                        if self.board[2] == " ":
                              board.set(valid_choices[2],self.sign)
                              print(valid_choices[2])
                              break  
                  elif self.self_win(board):
                        break
                  elif self.check_opponent_win(board):
                        break                                           
                  if self.board[4] == " ":
                        board.set(valid_choices[4],self.sign)
                        print(valid_choices[4])
                        break
                  elif self.self_win(board):
                        break
                  elif self.check_opponent_win(board):
                        break
                  elif self.board[6] == " ":
                        board.set(valid_choices[6],self.sign)
                        print(valid_choices[6])
                        break
                  elif self.self_win(board):
                        break
                  elif self.check_opponent_win(board):
                         break
                  elif self.board[1] == " ":
                        board.set(valid_choices[1],self.sign)
                        print(valid_choices[1])
                        break  
                  elif self.self_win(board):
                        break
                  
                  elif self.self_win(board):
                        break
                  elif self.check_opponent_win(board):
                         break
                  elif self.board[8] == " ":
                        board.set(valid_choices[8],self.sign)
                        print(valid_choices[8])
                        break
                  elif self.self_win(board):
                        break
                  elif self.check_opponent_win(board):
                        break
                  elif self.board[3] == " ":
                        board.set(valid_choices[3],self.sign)
                        print(valid_choices[3])
                        break
                  elif self.self_win(board):
                        break
                  elif self.check_opponent_win(board):
                        break
                  elif self.board[2] == " ":
                        board.set(valid_choices[2],self.sign)
                        print(valid_choices[2])
                        break
                  elif self.self_win(board):
                        break
                  elif self.check_opponent_win(board):
                        break
                  elif self.board[0] == " ":
                        board.set(valid_choices[0],self.sign)
                        print(valid_choices[0])
                        break
                  elif self.self_win(board):
                        break
                  
                  elif self.check_opponent_win(board):
                        break
                  
                  elif self.board[5] == " ":
                        board.set(valid_choices[5],self.sign)
                        print(valid_choices[5])
                        break
                  elif self.self_win(board):
                        break
                  elif self.check_opponent_win(board):
                        break
                  elif self.board[7] == " ":
                        board.set(valid_choices[7],self.sign)
                        print(valid_choices[7])
                        break
                  elif self.self_win(board):
                        break
                  elif self.check_opponent_win(board):
                        break

                 
            
            
            
                         
                              