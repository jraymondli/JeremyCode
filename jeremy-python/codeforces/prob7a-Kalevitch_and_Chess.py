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

if chessboardRows == ['BBBBBBBB', 'BBBBBBBB', 'BBBBBBBB', 'BBBBBBBB', 'BBBBBBBB', 'BBBBBBBB', 'BBBBBBBB', 'BBBBBBBB']:
    print '8'
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
