import re
file = open("input21.txt","r")
text = file.readlines()
file.close()

wds = "s.e "
keyword = re.compile(wds)

for line in text:
    if keyword.search (line):
       print line,
