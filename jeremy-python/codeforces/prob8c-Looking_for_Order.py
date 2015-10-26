import math
bag = raw_input().split(' ')
objects = int(raw_input())
objectsPos = []
objectsDist = []
holdCount = 0
objectsOrd = [0]
for x in range(objects):
    objectsPos.append(raw_input().split(' '))
while objects > 1:
    for x in range(objects):
        objectsDist.append(abs(int(objectsPos[0][x])) - abs(int(bag[0])) + abs(int(objectsPos[1][x])) - abs(int(bag[1])))
    heldObject = objectsDist.index(min(objectsDist))
    objectsOrd.append(objectsDist.index(min(objectsDist))+1)
    objects = objects - 1
    holdCount = holdCount + 1
    objectPos.pop([heldObject])







'''
objectsPos.pop(0)
objectsDist.pop(objectsDist.index(min(objectsDist)))
print objectsDist
if len(objectsPos) == 1:
    objectsOrd.append(objectsDist.index(min(objectsDist)))
    print objectsOrd


'''
