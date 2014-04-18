import re

file = open("file.html","r")
text = file.readlines()
file.close()
keyword = re.compile(r"html|body|title|br")

for line in text:
    if keyword.search (line):
       print line,

