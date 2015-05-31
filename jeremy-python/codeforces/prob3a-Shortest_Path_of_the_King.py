##################################################
# Answer to problem 3A, Shortest Path of the King
# Finds the shortest amount of moves from the first set to second set of coordinates based off of the kings movement
#
# Fully works, finished.
##################################################
xcoord = []
ycoord = []
direction_list = []
dict_getter = "'"
conversion_dictionary = { '\'a\'': 1,'\'b\'': 2,'\'c\'': 3,'\'d\'': 4,'\'e\'': 5,'\'f\'': 6,'\'g\'': 7,'\'h\'': 8}
for x in range(2):
    input = raw_input()
    y = ''.join(x for x in ("'", input[0], "'"))
    xcoord.append(conversion_dictionary.get(y))
    ycoord.append(int(input[1])) 
    ##################################################
    # Takes the coordinates of the king and the destination and sorts the letters into numbers
    ##################################################
if xcoord[0] == xcoord[1]:
    ycoord_diff = ycoord[0]-ycoord[1]
    if ycoord[0]-ycoord[1] > 0:
        for x in range(ycoord_diff):
            direction_list.append('D')
    else:                           
        for x in range(ycoord_diff * -1):
            direction_list.append('U')              
elif ycoord[0] == ycoord[1]:                  
    xcoord_diff = xcoord[0]-xcoord[1]
    if xcoord[0]-xcoord[1] > 0:
        for x in range(xcoord_diff):
            direction_list.append('L')                    
    else:                              
        for x in range(xcoord_diff * -1):
            direction_list.append('R')                     
    ##################################################
    # takes cases where destination is directly vertical/horizontal to king's position
    ##################################################
elif ycoord[0] > ycoord[1]:
        ##################################################
        # if the location is under the king:
        ##################################################
        if xcoord[0] > xcoord[1]:
            ##################################################
            #if the location is left of the king:
            ##################################################
            while ycoord[0] > ycoord[1] and xcoord[0] > xcoord[1]:
                direction_list.append("LD")
                ycoord[0] = ycoord[0]-1
                xcoord[0] = xcoord[0]-1
            while ycoord[0] > ycoord[1]:
                direction_list.append("D")
                ycoord[0] = ycoord[0] - 1
            while xcoord[0] > xcoord[1]:
                direction_list.append("L")
                xcoord[0] = xcoord[0] - 1
        elif xcoord[0] < xcoord[1]:
            ##################################################
            #if the location is right of the king:
            ##################################################
            while ycoord[0] > ycoord[1] and xcoord[0] < xcoord[1]:
                direction_list.append("RD")
                ycoord[0] = ycoord[0]-1
                xcoord[1] = xcoord[1]-1
            while ycoord[0] > ycoord[1]:
                direction_list.append("D")
                ycoord[0] = ycoord[0] - 1
            while xcoord[0] < xcoord[1]:
                direction_list.append("R")
                xcoord[0] = xcoord[0] + 1
        else:
            print "0"
elif ycoord[0] < ycoord[1]:
        ##################################################
        #if the location is above the king:                                                                          
        ##################################################
        if xcoord[0] > xcoord[1]:
            ##################################################
            #if the location is left of the king:             
            ##################################################
            while ycoord[0] < ycoord[1] and xcoord[0] > xcoord[1]:
                direction_list.append("LU")
                ycoord[0] = ycoord[0] + 1
                xcoord[0] = xcoord[0] - 1
            while ycoord[0] < ycoord[1]:
                direction_list.append("U")
                ycoord[0] = ycoord[0] + 1
            while xcoord[0] > xcoord[1]:
                direction_list.append("L")
                xcoord[0] = xcoord[0] - 1
        elif xcoord[0] < xcoord[1]:
            ##################################################
            #if the location is right of the king:            
            ##################################################
            while ycoord[0] < ycoord[1] and xcoord[0] < xcoord[1]:
                direction_list.append("RU")
                ycoord[0] = ycoord[0]+1
                xcoord[1] = xcoord[1]-1
            while ycoord[0] < ycoord[1]:
                direction_list.append("U")
                ycoord[0] = ycoord[0] + 1
            while xcoord[0] < xcoord[1]:
                direction_list.append("R")
                xcoord[0] = xcoord[0] + 1
        else:
            print "0"
counter = 0
print len(direction_list)
for x in range(len(direction_list)):
    print direction_list[counter]
    counter = counter + 1
################################################## 
# prints amount of steps and also the steps themselves
##################################################
