import re 
name_check = re.compile(r"[^A-Za-z\s\.]")
name = raw_input ("Enter your name: ")
while name_check.search(name):
    print "Enter your name correctly!"
    name = raw_input ("Enter your name: ")
address_check = re.compile(r"[^\w\s\.,]")
address = raw_input ("Please enter your address: ")
while address_check.search(address):
    print "Please enter your address correctly!"
    address = raw_input ("Please enter your address: ")
phone_check = re.compile(r"[^0-9\s\-\(\)]")
phone = raw_input ("Please enter your phone: ")
while phone_check.search(phone):
    print "Please enter your phone correctly!"
    phone = raw_input ("Please enter your phone: ")
