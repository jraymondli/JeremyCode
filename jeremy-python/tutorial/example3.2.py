import re
file = open("input3.2.txt","r")
text = file.readlines()
file.close()

wds = "\w[\W]\d"
keyword = re.compile(wds)

for line in text:
    if keyword.search (line):
       print line,
