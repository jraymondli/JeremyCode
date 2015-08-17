import sys
flagsForward = raw_input()
flagsBackward = flagsForward[::-1] 
awake1 = raw_input()
awake2 = raw_input()
len1 = len(awake1)
len2 = len(awake2)
forward = False
backward = False
if awake1+awake2 in flagsForward:
    forward = True
elif awake1 in flagsForward:
    for x in range(len(flagsForward)):
        if len(awake1) == 1:
            if awake1 in flagsForward[x]:
                pos1 = x
                break
        if len(awake1) > 1:
            if awake1 in flagsForward[:x]:
                pos1 = x
                break
    if awake2 in flagsForward[pos1:]:
        forward = True
if awake1+awake2 in flagsBackward:
    backward = True
elif awake1 in flagsBackward:
    for y in range(len(flagsBackward)):
        if len(awake1) == 1:
            if awake1 in flagsBackward[y]:
                pos2 = y
                break
        if len(awake1) > 1:
            if awake1 in flagsBackward[:y]:
                pos2 = y
                break
    if awake2 in flagsBackward[pos2:]:
        backward = True
print forward
print backward
if len(awake1)+len(awake2) > len(flagsForward):
    print "fantasy"
else:
    if forward == True and backward == False:
        print "forward"
    if forward == False and backward == True:
        print "backward"
    if forward == True and backward == True:
        print "both"
    if forward == False and backward == False:
        print "fantasy"
