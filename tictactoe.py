# CMPT 120 Intro to Programming
# Lab #7 – Lists and Error Handling
# Author: Susan Cantoni
# Created: 2018-03-26

symbol = [ " ", "x", "o" ]
board = [' ',' ',' ',
         ' ',' ',' ',
         ' ',' ',' ']

def printBoard(board):
    print('+-----------+')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('+-----------+')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('+-----------+')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('+-----------+')

def hasBlanks(board):
    # return true if any blank spaces left
    for cell in board:
        if cell == ' ':
            return True
    return False

def markBoard(board):
    player = 1
    while hasBlanks(board):
        choice = input('Player %d, select a spot(0-8): ' % player)
        choice = int(choice)
        if choice < 0 or choice > 8:
            print ("Please enter a number from 0 to 8")
        elif board[choice] != ' ':
            print ("This spot is taken! Pick a different spot. ")
        else:
            #assign space, switch to other player
            board[choice] = symbol[player]
            printBoard(board)
            if player == 1:
                player = 2
            else:
                player = 1

def main():
    printBoard(board)
    markBoard(board)

main()
