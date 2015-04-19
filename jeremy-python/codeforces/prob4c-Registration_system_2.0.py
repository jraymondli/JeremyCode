###############################################################################
# Second try at problem 4c registration system. Users are now being stored
# in a dictionary and repetive ones are the origional with their one added to
# their value. Then it is printed with the value. Much more efficient than 
# the first version.
# Lesson Learned:
# First think about the easiest way to get the solution instead of doing the 
# first idea that is thought of.
###############################################################################
a = input()
b = []
for x in range(a):
    b.append(raw_input())
d = {}
for k in b:
    c = k in d
    if c == False:
        d[k] = 0
        print "OK"
    else:
        d[k] = d[k] + 1
        e = str(d[k])
        f = ''.join(str(x) for x in (k,e))
        print(f)
