#Tic-tac-Toe

import random

def drawBoard(board):
    #this function prints out the board that it was passed
    # "board" is a list of 10 strings representing the board(ignore index 0)
    print(f"{board[7]} | {board[8]} | {board[9]}")
    print('-+-+-')
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print('-+-+-')
    print(f"{board[1]} | {board[2]} | {board[3]}")



def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
        #the first element in the list is the play'ers letter, 
        # the scond is the computers letter

        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

def whoGoeseFirst():
    #randomly choose who goese first
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    #given a board and a player's lettere, this function returns true if that player has run
    # be = board, le = letter 
    return (bo[7] == le and bo[8] == le and bo[9] == le) or # across top
    (bo[4] == le and bo[5] == le and bo[6] == le)




