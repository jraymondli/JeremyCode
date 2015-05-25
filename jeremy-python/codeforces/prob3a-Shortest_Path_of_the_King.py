xcoord = []
ycoord = []
dict_getter = "'"
conversion_dictionary = { '\'a\'': 1,'\'b\'': 2,'\'c\'': 3,'\'d\'': 4,'\'e\'': 5,'\'f\'': 6,'\'g\'': 7,'\'h\'': 8}
for x in range(2):
    input = raw_input()
    y = ''.join(x for x in ("'", input[0], "'"))
    xcoord.append(conversion_dictionary.get(y))
    ycoord.append(int(input[1])) 
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
elif ycoord[0] > ycoord[1]:
        if xcoord[0] > xcoord[1]:
            while ycoord[0] > ycoord[1] or xcoord[0] > xcoord[1]:
                print "LD"
                ycoord[0] = ycoord[0]-1
                xcoord[0] = xcoord[0]-1
                if xcoord[0] == xcoord[1]:
                    break
                if ycoord[0] == ycoord[1]:
                    break
            if ycoord[0] == ycoord[1]:
                while xcoord[0] != xcoord[1]:
                    print "D"
                    xcoord[0] = xcoord[0] + 1
            else:
                while ycoord[0] != ycoord[1]:
                    print "L"
                    ycoord[0] = ycoord[0] + 1
        elif xcoord[0] < xcoord[1]:
            print "unfinish"    
        else:
            while ycoord[0] > ycoord[1]:
                print "D"
                ycoord[0] = ycoord[0]-1
else:
    print "error"
'''            
elif xcoord[0] > xcoord[1]:
        if xcoord[0] > xcoord[1]:
            elif:
                xcoord[0] <xcoord[1]:
            else:
                while ycoord[0] > ycoord[1]:
                    print "D"
                    ycoord[0] = ycoord[0]-1
                    
'''

