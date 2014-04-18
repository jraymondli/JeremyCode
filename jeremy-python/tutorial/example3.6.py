import re
file = open("input3.6.txt","r")
text = file.readlines()
file.close()

wds = "\d\d?\.\d\d?\.\d\d"
keyword = re.compile(wds)

for line in text:
    if keyword.search (line):
       print line,

