# problem url:
# http://usaco.org/index.php?page=viewproblem2&cpid=104
import time
start_time = time.time()
instructions = raw_input().split(' ')
counter = 0
point = 0
value = 0
a = []
b = []
bales = [0]
bales = bales*int(instructions[0])
for x in range(int(instructions[1])):
    haybaleNumbers = raw_input().split(' ')
    a.append(int(haybaleNumbers[0]))
    b.append(int(haybaleNumbers[1]))
a.sort()
b.sort()

for x in range(int(instructions[0])):
    value = x+1
    print value
    for y in range(a.count(value)):
        a.remove(value)
        counter = counter + 1
    bales[x] = counter
    for y in range(b.count(value)):
        b.remove(value)
        counter= counter - 1

bales.sort()
print bales[(int(instructions[0])-1)/2]
print("--- %s seconds ---" % (time.time() - start_time))
