# Verion 1: uses less memory but more time
import array
number = int(input())
binaryList = array.array("i", range(number, 0, -1))
binaryList = [str(i) for i in binaryList]
count = len([s for s in binaryList if not s.strip('10')])
print count

# Version 2: uses more memory but less time
'''
number = int(input())
binaryList = range(number, 0, -1)
binaryList = [str(i) for i in binaryList]
count = len([s for s in binaryList if not s.strip('10')])
print count
'''

# I want to try and combine these lines:
'''
binaryList = array.array("i", range(number, 0, -1))
binaryList = [str(i) for i in binaryList]
'''
