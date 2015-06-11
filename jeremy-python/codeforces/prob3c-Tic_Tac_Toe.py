##################################################
# Answer to 3C, Tic-Tac-Toe
# It tells you whose turn it is on the tic tac toe board(if it is unfinished), who won, if the placements are illegal, or if it is a tie
#
# Fully works, finished
##################################################
import sys
board = []
win = 0
win1 = 0
win2 = 0
for x in range(3):
    listOfMoves = list(raw_input())
    board.append(listOfMoves[0])
    board.append(listOfMoves[1])
    board.append(listOfMoves[2])
##################################################                                                                                      
# Takes the input and stores it in a list.
################################################## 
if board[0] == board[1] == board[2] == 'X' or board[3] == board[4] == board[5] == 'X' or board[6] == board[7] == board[8] == 'X' or board[0] == board[3] == board[6] == 'X' or board[1] == board[4] == board[7] == 'X' or board[2] == board[5] == board[8] == 'X' or board[0] == board[4] == board[8] == 'X' or board[2] == board[4] == board[6] == 'X':
    win = win + 1
if board[0] == board[1] == board[2] == '0' or board[3] == board[4] == board[5] == '0' or board[6] == board[7] == board[8] == '0' or board[0] == board[3] == board[6] == '0' or board[1] == board[4] == board[7] == '0' or board[2] == board[5] == board[8] == '0' or board[0] == board[4] == board[8] == '0' or board[2] == board[4] == board[6] == '0':
    win = win + 1
##################################################                                                                    
# Checks for any three in a rows.                                                                             
################################################## 
elif board.count('X') != board.count('0')+1 and board.count('X') != board.count('0'):
    print "illegal"
    sys.exit()
elif win == 2:
    print "illegal"
    sys.exit()
################################################## 
# Checks if player 1 or 2 has taken too many turns and also checks if there has been two many wins, resulting in illegal boards.
################################################## 
if board.count('X') >= 3:
    if board[0] == board[1] == board[2] == 'X' or board[3] == board[4] == board[5] == 'X' or board[6] == board[7] == board[8] == 'X':
        win1 = "the first player won"
    elif board[0] == board[3] == board[6] == 'X' or board[1] == board[4] == board[7] == 'X' or board[2] == board[5] == board[8] == 'X':
        win1 = "the first player won"
    elif board[0] == board[4] == board[8] == 'X' or board[2] == board[4] == board[6] == 'X':
        win1 = "the first player won"
if board.count('0') >= 3:
    if board[0] == board[1] == board[2] == '0' or board[3] == board[4] == board[5] == '0' or board[6] == board[7] == board[8] == '0':
        win2 =  "the second player won"
    elif board[0] == board[3] == board[6] == '0' or board[1] == board[4] == board[7] == '0' or board[2] == board[5] == board[8] == '0':
        win2 =  "the second player won"
    elif board[0] == board[4] == board[8] == '0' or board[2] == board[4] == board[6] == '0':
        win2 =  "the second player won"
################################################## 
# If the board passes the legality tests, the official results are recorded for the three in a rows
################################################## 
if board.count('X') != board.count('0') and board.count('X') != board.count('0') + 1:
    print "illegal"
elif win1 == 0 and win2 == "the second player won":
    if board.count('0') < board.count('X'):
        print "illegal"
    else:
        print win2
elif win2 == 0 and win1 == "the first player won":
    if board.count('0') >= board.count('X'):
        print "illegal"
    else:
        print win1
elif win1 == "the first player won" and win2 == "the second player won":
    print "illegal"
elif  board.count('X') == board.count('0') and win1 == 0 and win2 == 0 and board.count('.') != 0:
    print "first"
elif board.count('X') == board.count('0') + 1 and win1 == 0 and win2 == 0 and board.count('.') != 0:
    print "second"
else:
    print 'draw'
################################################## 
# This makes sure that when the first or second player wins, the other player didn't take an extra turn.
# Also checks if both players have one or more three in a rows stimultaneously, resulting in an illegal board.
# If the board is incomplete, and has passed all the legality tests, then the turn of the next user is given
# Last, if the board fits none of the criteria above, a draw is called.
################################################## 
