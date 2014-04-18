file = open("alice.txt","r")
text = file.readlines()
file.close()

counter = 1
for line in text:
    print counter, line,
    counter = counter +1
print 
