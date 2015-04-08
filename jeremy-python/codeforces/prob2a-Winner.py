"""
L14:amount of lines(rounds)of game  
L15:list to store rounds of game
L16-17:splits the player and his score
L18:dictionary to store players and their scores
L19-20:seperates players and scores into keys and values. Also adds values of 
L19-20:the same player up.
L22:reverses the location of the key and values and stores them in a list
L23:gets one of the keys with the largest value 
L24:gets the largest value  
L25:resets d
L26-27:reruns value addition to determine tiebreakers
L28-30:checks for the first play to reach target value or above."""
a = input() 
b = []
for x in range(a):
    b.append(raw_input().split(' '))
d = {}
for k,v in b:
    d[k] = int(v) + int(d.get(k, 0))
inverse = [(value, key) for key, value in d.items()]
max_key = max(inverse)[1]
max_val = d.get(max_key, v)
d = {}
for k,v in b:
    d[k] = int(v) + int(d.get(k, 0))
    if d[k] >= max_val:
       answer = k
       break
print answer

    
