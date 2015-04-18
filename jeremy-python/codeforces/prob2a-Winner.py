##############################################################################
# Answer to codeforces problem 2A-Winner
# objective: find the person who gets the highest score first.
#
# The code first creates a variable to hold the number of rounds there is and 
# a list to hold the outcome of each round. Then puts the rounds in the list.
############################################################################## 
a = input() 
b = []
for x in range(a):
    b.append(raw_input().split(' '))
##############################################################################
# Then it turns the list into a dictionary and adds each player's points 
# together. After that, it gets the player who has the most points
##############################################################################
d = {}
for k,v in b:
    d[k] = int(v) + int(d.get(k, 0))
inverse = [(value, key) for key, value in d.items()]
max_key = max(inverse)[1]
max_val = d.get(max_key, v)
##############################################################################
# Last it resets the dictionary and replays the rounds to see who got the most 
# points first in case there was a tie, and then it print's the winner's name
##############################################################################
d = {}
for k,v in b:
    d[k] = int(v) + int(d.get(k, 0))
    if d[k] >= max_val:
       answer = k
       break
print answer

    
