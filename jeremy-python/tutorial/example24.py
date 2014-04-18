import re
file = open("input24.txt","r")
text = file.readlines()
file.close()

keyword = re.compile(r".")
for line in text:
     if keyword.search(line):
         print line,

keyword = re.compile(r" ")
for line in text:
     if keyword.search(line):
         print line,
