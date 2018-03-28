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

def markBoard(board):
    while True:
        choice1 = input('Player 1, select a spot: ')
        choice1 = int(choice1)
        
        if board[choice1] == 'x' or board[choice1] == 'o':
            print ("This spot is taken!")
            choice1 = input('Player 1, pick a different spot: ')
            choice1 = int(choice1)
            if board[choice1] != 'x' and board[choice1] != 'o':
                board[choice1] = 'x'

        elif board[choice1] != 'x' and board[choice1] != 'o':
            board[choice1] = 'x'
            
        printBoard(board)

        choice2 = input('Player 2, select a spot: ')
        choice2 = int(choice2)
        
        if board[choice2] == 'x' or board[choice2] == 'o':
            print ("This spot is taken!")
            choice2 = input('Player 2, pick a different spot: ')
            choice2 = int(choice2)
            if board[choice2] != 'x' and board[choice2] != 'o':
               board[choice2] = 'o'

        elif board[choice2] != 'x' and board[choice2] != 'o':
            board[choice2] = 'o'
            
        printBoard(board)

def main():
    printBoard(board)
    markBoard(board)

main()
