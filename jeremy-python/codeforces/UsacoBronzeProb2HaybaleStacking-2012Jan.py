import time

instructions = raw_input().split(' ')
bales = [0]
bales = bales*int(instructions[0])
for x in range(int(instructions[1])):
    
    haybaleNumbers = raw_input().split(' ')
    counter = int(haybaleNumbers[0])
    while counter <= int(haybaleNumbers[1]):
        bales[counter-1] = bales[counter-1] + 1
        counter = counter + 1
start_time = time.time()
print bales
bales.sort()
print bales[(int(instructions[0])-1)/2]
print("--- %s seconds ---" % (time.time() - start_time)) 


 
