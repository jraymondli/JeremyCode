board = []
for x in range(3):
    listOfMoves = list(raw_input())
    board.append(listOfMoves[0])
    board.append(listOfMoves[1])
    board.append(listOfMoves[2])
if board.count('X') != board.count('0')+1 and board.count('X') != board.count('0'):
    print "illegal"
elif board.count('X') >= 3 and board.count('.') == 0:
    if board[0] == board[1] == board[2] == 'X' or board[3] == board[4] == board[5] == 'X' or board[6] == board[7] == board[8] == 'X':
        print "the first player won"
    if board[0] == board[3] == board[6] == 'X' or board[1] == board[4] == board[7 == 'X'] or board[2] == board[5] == board[8] == 'X':
        print "the first player won"
    if board[0] == board[4] == board[8] == 'X' or board[2] == board[4] == board[6] == 'X':
        print "the first player won"
elif board.count('0') >= 3 and board.count('.') == 0:
    if board[0] == board[1] == board[2] == '0' or board[3] == board[4] == board[5] == '0' or board[6] == board[7] == board[8] == '0':
        print "the second player won"
    if board[0] == board[3] == board[6] == '0' or board[1] == board[4] == board[7] == '0' or board[2] == board[5] == board[8] == '0':
        print "the second player won"
    if board[0] == board[4] == board[8] == '0' or board[2] == board[4] == board[6] == '0':
        print "the second player won"
elif board.count('.') != 0:
    if board.count('X') == board.count('0') == 3:
        print 'illegal'
    elif board.count('X') == board.count('0'):
        print "first"
    elif board.count('X') == board.count('0') + 1:
        print "second"
    else:
        print "illegal"
else:
    print 'draw'
