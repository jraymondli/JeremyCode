alice = 0
bob = 0
bars = int(input())
times = raw_input().split(' ')
counter = 0
totalTime = 0
for x in range(bars):
    totalTime = totalTime + int(times[counter])
    counter = counter + 1
counter1 = 0
counter2 = 0
a = 0
b = 0
#print bars
for x in range(bars):
    if alice < bob:
        a = a + 1 
        alice = alice + int(times[counter1])
        #print'alice', alice
        counter1 = counter1 + 1
    elif alice > bob:
        b = b + 1
        bob = bob + int(times[bars - counter2 - 1])
        #print 'bob', bob
        counter2 = counter2 + 1
    elif alice == bob:
        a = a + 1
        alice = alice + int(times[counter1])
        #print 'equal', alice
        counter1 = counter1 + 1
print a, b


