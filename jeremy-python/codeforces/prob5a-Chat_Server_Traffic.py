###############################################################################
# This handles a chat traffic. every time someone siends a message, you 
# multiply the message length by the aout of people online.
# players coming on and off are marked by +<name> and -<name>
# messages are in <name>:<msg> The code counts the message length and 
# multiplies it by the amount of people on and adds it to the current amount of
# traffic.
###############################################################################
e = 0
d = 0
y = 0
for x in range(7):
    try:
        a = raw_input()
    except EOFError:
        break
    if a[:1] == '+':
        y = y + 1
    elif a[:1] == '-':
        y = y - 1
    else:
        a = a.split(':')
        b = a[1]
        e = 0
        e = e + len(b)
        e = e*y
        d = d + e
print d

