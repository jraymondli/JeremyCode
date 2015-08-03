##################################################                                                         
# Solution for problem 7a Kalevitch and Chess                                              
# http://codeforces.com/contest/7/problem/A
# This gives the number of strokes needed to paint a specific pattern onto a white 8 by 8 board.
# The strokes are vertical and horizontal, one tile thick, black and eight tiles long.
##################################################
chessboardRows = []
strokes = 0
strokePosition = []
for x in range(8):
    input = raw_input()
    chessboardRows.append(input)
##################################################
# The above takes the pattern of the board.
##################################################
if chessboardRows == ['BBBBBBBB', 'BBBBBBBB', 'BBBBBBBB', \
'BBBBBBBB', 'BBBBBBBB', 'BBBBBBBB', 'BBBBBBBB', 'BBBBBBBB']:
    print '8'
    ##################################################
    # the above covers the iteration of a fully black board.
    ##################################################
else:
    strokes = 0
    for x in range(8):
        if 'B' == chessboardRows[0][counter] ==\ 
        chessboardRows[1][x] == chessboardRows[2][x] ==\
        chessboardRows[3][x] == chessboardRows[4][x] ==\
        chessboardRows[5][x] == chessboardRows[6][x] ==\ 
        chessboardRows[7][x]:
            strokes = strokes + 1
    for x in range(8): 
        if 'B' == chessboardRows[counter][0] ==\ 
        chessboardRows[x][1] == chessboardRows[x][2] ==\ 
        chessboardRows[x][3] == chessboardRows[x][4] ==\ 
        chessboardRows[x][5] == chessboardRows[x][6] ==\
        chessboardRows[x][7]:
            strokes = strokes + 1
    print strokes
##################################################
# The rest of the code accounts for calculating the amount of strokes nessesary.
# It does the by checking for complete black rows/columns.
##################################################
