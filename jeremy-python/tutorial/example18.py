import re
file = open("alice.txt","r")
text = file.readlines()
file.close()

keyword = re.compile(r"the ")

for line in text:
    if not keyword.search (line):
       print line,

