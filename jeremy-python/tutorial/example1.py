import sys
print("input temp in Faren")
user_input = sys.stdin.readline()
print user_input
Fdegrees = int(user_input)
#Fdegrees = int(sys.stdin.readline())
Cdegrees = (Fdegrees - 32) * 5/9
print (Cdegrees)
