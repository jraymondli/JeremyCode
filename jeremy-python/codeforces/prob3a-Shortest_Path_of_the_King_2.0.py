xcoord = []
ycoord = []
dict_getter = "'"
conversion_dictionary = { '\'a\'': 1,'\'b\'': 2,'\'c\'': 3,'\'d\'': 4,'\'e\'': 5,'\'f\'': 6,'\'g\'': 7,'\'h\'': 8}
for x in range(2):
    input = raw_input()
    y = ''.join(x for x in ("'", input[0], "'"))
    xcoord.append(conversion_dictionary.get(y))
    ycoord.append(int(input[1]))
if xcoord[0] > xcoord[1]:
    if ycoord[0] > ycoord[1]:
        direction = 'DL'
    elif ycoord[0] < ycoord[1]:
        direction = 'UL'
    else:
        direction = 'L'
elif xcoord[0] <  xcoord[1]:
    if ycoord[0] > ycoord[1]:
        direction = 'DR'
    elif ycoord[0] < ycoord[1]:
        direction = 'UR'
    else:
        direction = 'R'
else:
    if ycoord[0] > ycoord[1]:
        direction = 'D'
    elif:
        direction = 'U' 
    direction = 0
if xcoord[0] == xcoord[1]:
    ycoord_diff = ycoord[0]-ycoord[1]
    if ycoord[0]-ycoord[1] > 0:
        for x in range(ycoord_diff):
            print 'D'
    else:
        for x in range(ycoord_diff * -1):
            print 'U'
elif ycoord[0] == ycoord[1]:
    xcoord_diff = xcoord[0]-xcoord[1]
    if xcoord[0]-xcoord[1] > 0:
        for x in range(xcoord_diff):
            print 'L'
    else:
        for x in range(xcoord_diff * -1):
            print 'R'
else:
    while xcoord[0] != xcoord[1] or ycoord[0] != ycoord[1]:
        
