flagsForward = raw_input()
flagsBackward = flagsForward[::-1] 
awake1 = raw_input()
awake2 = raw_input()
len1 = len(awake1)
len2 = len(awake2)
forward = False
backward = False
if awake1 in flagsForward:
    pos1 = flagsForward.index(awake1)
    if awake2 in flagsForward[pos1-1+len(awake1):]:
        forward = True
if awake1 in flagsBackward:
    pos2 = flagsBackward.index(awake1)
    if awake2 in flagsBackward[pos2-1+len(awake1):]:
        backward = True
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
