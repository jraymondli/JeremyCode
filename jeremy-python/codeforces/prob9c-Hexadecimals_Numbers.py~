# Verion 1: uses less memory but more time
'''
import array
number = int(input())
binaryList = array.array("i", range(number, 0, -1))
binaryList = [str(i) for i in binaryList]
count = len([s for s in binaryList if not s.strip('10')])
print count
'''
# Version 2: uses more memory but less time
'''
number = int(input())
binaryList = range(number, 0, -1)
binaryList = [str(i) for i in binaryList]
count = len([s for s in binaryList if not s.strip('10')])
print count
'''
# Version 3: Comparison between decimal & binary numbers-success 
number = input()
lenNumb = len(str(number))
count = 0
for x in range(2**lenNumb - 1):
    if int(str(bin(x+1))[2:]) <= number:
        count = count + 1
print count


