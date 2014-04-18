import re
file = open("input3.5.txt","r")
text = file.readlines()
file.close()

wds = "(the)+"
keyword = re.compile(wds)

for line in text:
    if keyword.search (line):
       print line,
