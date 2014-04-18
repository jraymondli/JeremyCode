import re
file = open("input3.3.txt","r")
text = file.readlines()
file.close()

wds = "[A-Z][a-zA-Z]+ "
keyword = re.compile(wds)

for line in text:
    if keyword.search (line):
       print line,
