import re
file = open("input3.1.txt","r")
text = file.readlines()
file.close()

wds = "[13579][2468]"
keyword = re.compile(wds)

for line in text:
    if keyword.search (line):
       print line,
