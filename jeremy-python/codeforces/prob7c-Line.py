line = raw_input().split(' ')
A = int(line[0])
B = int(line[1])
C = int(line[2])
if A == 0:
    if float(-C)/float(B)+C/B == 0 or 0.0:
        print 0, -C/B
    else:
        print -1
elif B == 0:
    if float(-C)/float(A)+C/A == 0 or 0.0:
        print -C/A, 0
    else:
        print -1
elif C == 0:
    print 0, 0
else:
    x = 0
    y = float(-C-A*x)/float(B)
    while y != int or x < 10:
        y = float(-C-A*x)/float(B)
        if y - int(y) == 0:
            break
        x = x + 1
    if x < 10:
        print x, int(y)
    else:
        print -1
