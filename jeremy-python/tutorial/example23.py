import re
file = open("input23.txt","r")
text = file.readlines()
file.close()

wds = "^a.+[ n]"
keyword = re.compile(wds)

for line in text:
    if not keyword.search (line):
       print line,
