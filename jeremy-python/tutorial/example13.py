file = open("alice.txt","r")
text = file.readlines()
file.close()
print text

text.reverse()

for line in text:
    print line,
print 


