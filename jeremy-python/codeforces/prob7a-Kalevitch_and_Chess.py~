##################################################                                                         
# Solution for problem 7a Kalevitch and Chess                                              
# http://codeforces.com/contest/7/problem/A
# This gives the number of strokes needed to paint a specific pattern onto a white 8 by 8 board.
# The strokes are vertical and horizontal, one tile thick, black and eight tiles long.
##################################################
chessboardRows = []
strokes = 0
strokePosition = []
counter = 0
for x in range(8):
    input = raw_input()
    chessboardRows.append(input)
    if 'B' in (input[0]):
        strokes = strokes + 1
for x in range(8):
    if 'B' in chessboardRows[0][counter] and strokes != 8:
        strokes = strokes + 1
    counter = counter + 1
##################################################
# The above takes the pattern of the board.
##################################################
if chessboardRows == ['BBBBBBBB', 'BBBBBBBB', 'BBBBBBBB', 'BBBBBBBB', 'BBBBBBBB', 'BBBBBBBB', 'BBBBBBBB', 'BBBBBBBB']:
    print '8'
    ##################################################
    # the above covers the iteration of a fully black board.
    ##################################################
else:
    strokes = 0
    counter = 0
    for x in range(8):
        if 'B' == chessboardRows[0][counter] == chessboardRows[1][counter] == chessboardRows[2][counter] == chessboardRows[3][counter] == chessboardRows[4][counter] == chessboardRows[5][counter] == chessboardRows[6][counter] == chessboardRows[7][counter]:
            strokes = strokes + 1
        counter = counter + 1
    counter = 0
    for x in range(8): 
        if 'B' == chessboardRows[counter][0] == chessboardRows[counter][1] == chessboardRows[counter][2] == chessboardRows[counter][3] == chessboardRows[counter][4] == chessboardRows[counter][5] == chessboardRows[counter][6] == chessboardRows[counter][7]:
            strokes = strokes + 1
        counter = counter + 1
    print strokes
##################################################
# The rest of the code accounts for calculating the amount of strokes nessesary.
# It does the by checking for complete black rows/columns.
##################################################
