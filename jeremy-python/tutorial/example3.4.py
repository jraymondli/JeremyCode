import re
file = open("input3.4.txt","r")
text = file.readlines()
file.close()

wds = "[yY][Ee][sS]"
keyword = re.compile(wds)

for line in text:
    if keyword.search (line):
       print line,
