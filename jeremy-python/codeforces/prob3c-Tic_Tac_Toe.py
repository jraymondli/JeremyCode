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
if board[0] == board[1] == board[2] == 'X' or board[3] == board[4] == board[5] == 'X' or board[6] == board[7] == board[8] == 'X' or board[0] == board[3] == board[6] == 'X' or board[1] == board[4] == board[7] == 'X' or board[2] == board[5] == board[8] == 'X' or board[0] == board[4] == board[8] == 'X' or board[2] == board[4] == board[6] == 'X':
    win = win + 1
if board[0] == board[1] == board[2] == '0' or board[3] == board[4] == board[5] == '0' or board[6] == board[7] == board[8] == '0' or board[0] == board[3] == board[6] == '0' or board[1] == board[4] == board[7] == '0' or board[2] == board[5] == board[8] == '0' or board[0] == board[4] == board[8] == '0' or board[2] == board[4] == board[6] == '0':
    win = win + 1
#
elif board.count('X') != board.count('0')+1 and board.count('X') != board.count('0'):
    print "illegal"
    sys.exit()
elif win == 2:
    print "illegal"
    sys.exit()
#
if board.count('X') >= 3:
    if board[0] == board[1] == board[2] == 'X' or board[3] == board[4] == board[5] == 'X' or board[6] == board[7] == board[8] == 'X':
        win1 = "the first player won"
    elif board[0] == board[3] == board[6] == 'X' or board[1] == board[4] == board[7] == 'X' or board[2] == board[5] == board[8] == 'X':
        win1 =  "the first player won"
    elif board[0] == board[4] == board[8] == 'X' or board[2] == board[4] == board[6] == 'X':
        win1 = "the first player won"
if board.count('0') >= 3:
    if board[0] == board[1] == board[2] == '0' or board[3] == board[4] == board[5] == '0' or board[6] == board[7] == board[8] == '0':
        win2 =  "the second player won"
    elif board[0] == board[3] == board[6] == '0' or board[1] == board[4] == board[7] == '0' or board[2] == board[5] == board[8] == '0':
        win2 =  "the second player won"
    elif board[0] == board[4] == board[8] == '0' or board[2] == board[4] == board[6] == '0':
        win2 =  "the second player won"

#
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
