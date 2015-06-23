##################################################
# Solution for prob 6b, President's office
# unfinished, on test 18
##################################################
layout = []
prezDeskY = []
prezDeskX = []
X = False
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
    if len(prezDeskY) > 1 and deskCounterY + 1 < len(prezDeskY):
        deskCounterY = deskCounterY + 1
deskCounter = 0
deskCounterY = 0
print prezDeskY
for x in range(len(prezDeskX)*len(prezDeskY)):
        try:
            subDeskFinder = layout[prezDeskY[deskCounterY]-1][prezDeskX[deskCounter]]
            #print subDeskFinder
            if subDeskFinder != '.' and subDeskFinder not in subDeskList and prezDeskX[deskCounter] >= 0 and prezDeskY[deskCounterY]-1 >= 0:
                subordinates = subordinates + 1
                subDeskList.append(layout[prezDeskY[deskCounterY]-1][prezDeskX[deskCounter]])
                #print '[1]'
        except IndexError:
            subordinates = subordinates
        try:
            subDeskFinder = layout[prezDeskY[deskCounterY]+1][prezDeskX[deskCounter]]
            #print subDeskFinder
            if subDeskFinder != '.' and subDeskFinder not in subDeskList and prezDeskX[deskCounter] >= 0:
                subordinates = subordinates + 1
                subDeskList.append(layout[prezDeskY[deskCounterY]+1][prezDeskX[deskCounter]])
                #print '[2]'
        except IndexError:
            subordinates = subordinates
        try:
            subDeskFinder = layout[prezDeskY[deskCounterY]][prezDeskX[deskCounter]-1]
            #print subDeskFinder
            if subDeskFinder != '.' and subDeskFinder not in subDeskList and prezDeskX[deskCounter]-1 >= 0:
                subordinates = subordinates + 1
                subDeskList.append(layout[prezDeskY[deskCounterY]][prezDeskX[deskCounter]-1])
                #print '[3]'
        except IndexError:
            subordinates = subordinates
        try:
            subDeskFinder = layout[prezDeskY[deskCounterY]][prezDeskX[deskCounter]+1]
            #print subDeskFinder
            if subDeskFinder != '.' and subDeskFinder not in subDeskList and prezDeskX[deskCounter] >= 0:
                subordinates = subordinates + 1
                subDeskList.append(layout[prezDeskY[deskCounterY]][prezDeskX[deskCounter]+1])
                #print '[4]'
        except IndexError:
            subordinates = subordinates
        if len(prezDeskX) > 1 and deskCounter < len(prezDeskX)-1:
            deskCounter = deskCounter + 1
        else:
            X = True
        if len(prezDeskY) > 1 and deskCounterY < len(prezDeskY)-1 and X == True:
            deskCounterY = deskCounterY + 1
            deskCounter = 0
            X = False
print subDeskList
print subordinates
