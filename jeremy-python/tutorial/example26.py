import re
file = open("input26.txt","r")
text = file.readlines()
file.close()

wds = " +"
keyword = re.compile(wds)

for line in text:
    if keyword.search (line):
       print line,
