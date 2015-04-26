b = []
c = {}
e = 0
f = 0
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

