##################################################
# Solution for prob 6b, President's office
# finished, on test 20
#
# This problem counts the number of desks that share a side with the president's desk(known as his associates). 
##################################################
layout = []
prezDeskY = []
prezDeskX = []
X = False
deskCounter = 0
subordinates = 0
coordinatesAndColor = raw_input().split(' ')
################################################## 
# The first line of input gives the dimensions of the room the desks are in, and then the color of the President's desk.
# (Every desk has a unique color and is a rectangle with sides parallel to the room)
################################################## 
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
################################################## 
# Checks rows for president's desk
################################################## 
deskCounter = 0
deskCounterY = 0
for x in range(len(layout[prezDeskY[0]])):
    if layout[prezDeskY[deskCounterY]][deskCounter] == Color:
        prezDeskX.append(deskCounter)
    deskCounter = deskCounter + 1
    if len(prezDeskY) > 1 and deskCounterY + 1 < len(prezDeskY):
        deskCounterY = deskCounterY + 1
################################################## 
# Checks the letters in the rows with the prezident's desk color
##################################################  
deskCounter = 0
deskCounterY = 0
print prezDeskY
for x in range(len(prezDeskX)*len(prezDeskY)):
        try:
            subDeskFinder = layout[prezDeskY[deskCounterY]-1][prezDeskX[deskCounter]]
            if subDeskFinder != '.' and subDeskFinder not in subDeskList and prezDeskX[deskCounter] >= 0 and prezDeskY[deskCounterY]-1 >= 0:
                subordinates = subordinates + 1
                subDeskList.append(layout[prezDeskY[deskCounterY]-1][prezDeskX[deskCounter]])
        except IndexError:
            subordinates = subordinates
        try:
            subDeskFinder = layout[prezDeskY[deskCounterY]+1][prezDeskX[deskCounter]]
            if subDeskFinder != '.' and subDeskFinder not in subDeskList and prezDeskX[deskCounter] >= 0:
                subordinates = subordinates + 1
                subDeskList.append(layout[prezDeskY[deskCounterY]+1][prezDeskX[deskCounter]])
        except IndexError:
            subordinates = subordinates
        try:
            subDeskFinder = layout[prezDeskY[deskCounterY]][prezDeskX[deskCounter]-1]
            if subDeskFinder != '.' and subDeskFinder not in subDeskList and prezDeskX[deskCounter]-1 >= 0:
                subordinates = subordinates + 1
                subDeskList.append(layout[prezDeskY[deskCounterY]][prezDeskX[deskCounter]-1])
        except IndexError:
            subordinates = subordinates
        try:
            subDeskFinder = layout[prezDeskY[deskCounterY]][prezDeskX[deskCounter]+1]
            if subDeskFinder != '.' and subDeskFinder not in subDeskList and prezDeskX[deskCounter] >= 0:
                subordinates = subordinates + 1
                subDeskList.append(layout[prezDeskY[deskCounterY]][prezDeskX[deskCounter]+1])
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
################################################## 
# The code above checks the front, back, left, and right of the president's desk for other desks.
# If there is a new and unique color, 1 is added to the total associates
# The try-except loops are for when there is an IndexError(when there is a wall next to the president's desk)
# The last 8 lines of this part cycle through each tile of the presidents desk. 
#
# Below: The number of associates printed
###################################################
print subordinates
