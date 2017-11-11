"""
Tic - Tac - Toe AI
Created by Thomas Patton <tjpatton1@gmail.com>
Copyright 2017
"""

import random

#This function makes sure the user inputs valid inputs for row and column selection 
def get_valid_index(prompt):
    while True:
        try:
            index = int(input(prompt))
            if index >= 1 and index <= 3:
                return index
            print("Must be 1 - 3 inclusive!")
        except:
            print("Must be an integer!")

#Checks for the end of the game by surveysing horizontal, vertical, and diagonal
def game_is_over(board):
    for i in range(3):
        # Check horizontal
        if board[i][0] == board[i][1] == board[i][2] \
            and board[i][0] != " ":
            print(board[i][0] + " wins!")
            return True
        
        # Check vertical
        if board[0][i] == board[1][i] == board[2][i] \
            and board[0][i] != " ":
            print(board[0][i] + " wins!")
            return True
        
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] \
        and board[0][0] != " ":
        print(board[0][0] + " wins!")
        return True
    
    if board[2][0] == board[1][1] == board[0][2] \
        and board[2][0] != " ":
        print(board[2][0] + " wins!")
        return True
    
    # Check tie
    if " " not in board[0] and " " not in board[1] \
        and " " not in board[2]:
        print("Tie game!")
        return True
    
    # Not over yet!
    return False
    
# A function to print the 3x3 2D list and make it look like a board
def print_board(board):
    for item in board:
        print(item)

#Creates a 3x3 board
board = []
for i in range(3):
    board.append([" "] * 3)


# x goes first
turn = "x"

#This function determines the computer's move choice. It begins with an attacking section which checks for a computer win condition, and then goes to a defensive section which attempts to stop the player from winning.
def computer():
  guessx = 0
  guessy = 0
  
  #This section of code enters the defensive section. If the computer does not detect a possible win condition from the attack section, it will then go into the defensive and attempt to stop the player's win condition..
  #horizontal
  for i in range(3):
    if board[i][0] == "x" and board[i][1] == "x" and board[i][2] == " ":
      guessx = i
      guessy = 2
    if board[i][0] == "x" and board[i][2] == "x" and board[i][1] == " ":
      guessx = i
      guessy = 1
    if board[i][1] == "x" and board[i][2] == "x" and board[i][0] == " ":
      guessx = i
      guessy = 0
  
  #vertical
  for i in range(3):
    if board[0][i] == "x" and board[1][i] == "x" and board[2][i] == " ":
      guessx = 2
      guessy = i
    if board[0][i] == "x" and board[2][i] == "x" and board[1][i] == " ":
      guessx = 1
      guessy = i
    if board[1][i] == "x" and board[2][i] == "x" and board[i][0] == " ":
      guessx = 0
      guessy = i
  
  #diagonal
  if board[0][0] == "x" and board[1][1] == "x" and board[2][2] == " ":
    guessx = 2
    guessy = 2
  if board[0][0] == "x" and board[2][2] == "x" and board[1][1] == " ":
    guessx = 1
    guessy = 1
  if board[1][1] == "x" and board[2][2] == "x" and board[0][0] == " ":
    guessx = 0
    guessy = 0
  if board[0][2] == "x" and board[1][1] == "x" and board[2][0] == " ":
    guessx = 2
    guessy = 0
  if board[0][2] == "x" and board [2][0] == "x" and board[1][1] == " ":
    guessx = 1
    guessy = 1
  if board[2][0] == "x" and board[1][1] == "x" and board[0][2] == " ":
    guessx = 0
    guessy = 2
    
  #This begins the attack section
  #horizontal
  for i in range(3):
    if board[i][0] == "o" and board[i][1] == "o" and board[i][2] == " ":
      guessx = i
      guessy = 2
    if board[i][0] == "o" and board[i][2] == "o" and board[i][1] == " ":
      guessx = i
      guessy = 1
    if board[i][1] == "o" and board[i][2] == "o" and board[i][0] == " ":
      guessx = i
      guessy = 0
  
  #vertical
  for i in range(3):
    if board[0][i] == "o" and board[1][i] == "o" and board[2][i] == " ":
      guessx = 2
      guessy = i
    if board[0][i] == "o" and board[2][i] == "o" and board[1][i] == " ":
      guessx = 1
      guessy = i
    if board[1][i] == "o" and board[2][i] == "o" and board[i][0] == " ":
      guessx = 0
      guessy = i
  
  #diagonal
  if board[0][0] == "o" and board[1][1] == "o" and board[2][2] == " ":
    guessx = 2
    guessy = 2
  if board[0][0] == "o" and board[2][2] == "o" and board[1][1] == " ":
    guessx = 1
    guessy = 1
  if board[1][1] == "o" and board[2][2] == "o" and board[0][0] == " ":
    guessx = 0
    guessy = 0
  if board[0][2] == "o" and board[1][1] == "o" and board[2][0] == " ":
    guessx = 2
    guessy = 0
  if board[0][2] == "o" and board [2][0] == "o" and board[1][1] == " ":
    guessx = 1
    guessy = 1
  if board[2][0] == "o" and board[1][1] == "o" and board[0][2] == " ":
    guessx = 0
    guessy = 2
  else:
    while board[guessx][guessy]  != " ":
      guessx = random.randint(0,2)
      guessy = random.randint(0,2)
  
  board[guessx][guessy] = "o"

# main function, runs the tic-tac-toe
for i in range(9):
    print_board(board)
    print("Your turn ")
    selection = ""
    
    while selection != " ":
      row = get_valid_index("Row: ")
      col = get_valid_index("Col: ")
      selection = board[row - 1][col - 1]
    
    if board[row - 1][col - 1] == " ":
        board[row - 1][col - 1] = "x"
    else:
        print("Space is filled :(")
        
    if game_is_over(board) == True:
        print_board(board)
        break
      
    computer()

    if game_is_over(board) == True:
        print_board(board)
        break
