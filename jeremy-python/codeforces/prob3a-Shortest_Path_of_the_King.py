##################################################
# Answer to problem 3A, Shortest Path of the King
# Finds the shortest amount of moves from the first set to second set of coordinates based off of the kings movement
#
# currently works, but not ready for formal testing
# must put answers into a list, print the amount of items in the list then the items in the list itself.
# more comments will be added in final version
##################################################
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
        #if the location is under the king
        if xcoord[0] > xcoord[1]:
            #if the location is left of the king
            while ycoord[0] > ycoord[1] and xcoord[0] > xcoord[1]:
                print "LD"
                ycoord[0] = ycoord[0]-1
                xcoord[0] = xcoord[0]-1
            while ycoord[0] > ycoord[1]:
                print "D"
                ycoord[0] = ycoord[0] - 1
            while xcoord[0] > xcoord[1]:
                print "L"
                xcoord[0] = xcoord[0] - 1
        elif xcoord[0] < xcoord[1]:
            #if the location is right of the king
            while ycoord[0] > ycoord[1] and xcoord[0] < xcoord[1]:
                print "RD"
                ycoord[0] = ycoord[0]-1
                xcoord[1] = xcoord[1]-1
            while ycoord[0] > ycoord[1]:
                print "D"
                ycoord[0] = ycoord[0] - 1
            while xcoord[0] < xcoord[1]:
                print "R"
                xcoord[0] = xcoord[0] + 1
        else:
            print"0"
elif ycoord[0] < ycoord[1]:
        #if the location is above the king                                                                           
        if xcoord[0] > xcoord[1]:
            #if the location is left of the king                                      
            while ycoord[0] < ycoord[1] and xcoord[0] > xcoord[1]:
                print "LU"
                ycoord[0] = ycoord[0] + 1
                xcoord[0] = xcoord[0] - 1
            while ycoord[0] < ycoord[1]:
                print "U"
                ycoord[0] = ycoord[0] + 1
            while xcoord[0] > xcoord[1]:
                print "L"
                xcoord[0] = xcoord[0] - 1
        elif xcoord[0] < xcoord[1]:
            #if the location is right of the king                                                                   
            while ycoord[0] < ycoord[1] and xcoord[0] < xcoord[1]:
                print "RU"
                ycoord[0] = ycoord[0]+1
                xcoord[1] = xcoord[1]-1
            while ycoord[0] < ycoord[1]:
                print "U"
                ycoord[0] = ycoord[0] + 1
            while xcoord[0] < xcoord[1]:
                print "R"
                xcoord[0] = xcoord[0] + 1
        else:
            print "0"



