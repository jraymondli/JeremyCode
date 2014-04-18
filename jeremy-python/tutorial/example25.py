import re
file = open("input25.txt","r")
text = file.readlines()
file.close()

wds = " +"
keyword = re.compile(wds)

for line in text:
    if not keyword.search (line):
       print line,
