##################################################
# Solution for prob 6b, President's office
# unfinished, on test 8
##################################################
layout = []
prezDeskY = []
prezDeskX = []
deskCounter = 0
subordinates = 0
coordinatesAndColor = raw_input().split(' ')
Color = coordinatesAndColor[2]
YRange = int(coordinatesAndColor[0])
XRange = int(coordinatesAndColor[1])
subDeskList = [Color]
for x in range(YRange):
    input = raw_input()
    layout.append(input)
    counter = Color in input
    if counter == True:
        prezDeskY.append(deskCounter)
    deskCounter = deskCounter + 1
deskCounter = 0
deskCounterY = 0
for x in range(len(layout[prezDeskY[0]])):
    if layout[prezDeskY[deskCounterY]][deskCounter] == Color:
        prezDeskX.append(deskCounter)
    deskCounter = deskCounter + 1
    if len(prezDeskY) > 1 and deskCounterY < len(prezDeskY):
        deskCounterY = deskCounterY + 1
deskCounter = 0
deskCounterY = 0
for x in range(len(prezDeskX)*len(prezDeskY)):
        try:
            subDeskFinder = layout[prezDeskY[deskCounterY]-1][prezDeskX[deskCounter]]
            if subDeskFinder != '.' and subDeskFinder not in subDeskList:
                subordinates = subordinates + 1
                subDeskList.append(layout[prezDeskY[deskCounterY]-1][prezDeskX[deskCounter]])
        except IndexError:
            subordinates = subordinates
        try:
            subDeskFinder = layout[prezDeskY[deskCounterY]+1][prezDeskX[deskCounter]]
            if subDeskFinder != '.' and subDeskFinder not in subDeskList:
                subordinates = subordinates + 1
                subDeskList.append(layout[prezDeskY[deskCounterY]+1][prezDeskX[deskCounter]])
        except IndexError:
            subordinates = subordinates
        try:
            subDeskFinder = layout[prezDeskY[deskCounterY]][prezDeskX[deskCounter]-1]
            if subDeskFinder != '.' and subDeskFinder not in subDeskList:
                subordinates = subordinates + 1
                subDeskList.append(layout[prezDeskY[deskCounterY]][prezDeskX[deskCounter]-1])
        except IndexError:
            subordinates = subordinates
        try:
            subDeskFinder = layout[prezDeskY[deskCounterY]][prezDeskX[deskCounter]+1]
            if subDeskFinder != '.' and subDeskFinder not in subDeskList:
                subordinates = subordinates + 1
                subDeskList.append(layout[prezDeskY[deskCounterY]][prezDeskX[deskCounter]+1])
        except IndexError:
            subordinates = subordinates
        if len(prezDeskX) > 1 and deskCounter < len(prezDeskX):
            deskCounter = deskCounter + 1
        if len(prezDeskY) > 1 and deskCounterY < len(prezDeskY):
            deskCounterY = deskCounterY + 1
print subordinates
 
