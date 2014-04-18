import re

file = open("file.html","r")
text = file.readlines()
file.close()
keyword = re.compile(r"(.)(.*)(.)")

for line in text:
    if keyword.search (line):
       print line,

