alice = 0         
bob = 0           
bars = int(input())
times = raw_input().split(' ')
counter = 0
totalTime = 0
for x in range(bars):
    totalTime = totalTime + int(times[counter])
    counter = counter + 1
counter = 0
a = 0
b = 0 
while a + b + 1 < bars:
    if alice == bob:
        alice = alice + int(times[counter])
        #print "1", times[counter]
        a = a + 1        
    elif alice < bob:
        alice = alice + int(times[counter])
        a = a + 1
        #print "2", times[counter]
    if alice > bob:
        bob = bob + int(times[bars - counter - 1])
        b = b + 1
        #print "3", times[bars - counter - 1]
    counter = counter + 1

#print a, b
#print alice, bob
if a + b != bars:
    if alice > bob:
        b = b + 1
    elif alice < bob:
        a = a + 1
    elif alice == bob:
        a = a + 1
print a, b
print alice, bob
