import re
file = open("alice.txt","r")
text = file.readlines()
file.close()

keyword = re.compile(r"oo")

for line in text:
    if keyword.search (line):
       print line,
