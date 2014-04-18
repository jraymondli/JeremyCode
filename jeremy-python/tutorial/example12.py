import sys

studentlist = ["Alan","Andrew","Amanda","Angela","Anthony"]
print studentlist
student6 = raw_input("Input another student name; ")
studentlist.append(student6)
print studentlist
print"input a number less than 6"
numb = int(sys.stdin.readline())
print studentlist[numb]
studentlist = ["John Smith","Mary Miller"] + studentlist
print studentlist
studentlist.remove(student6)
print studentlist
name = raw_input("Type in a name; ")
if name == studentlist[0]:
    studentlist.remove(studentlist[0])
elif name == studentlist[1]:
    studentlist.remove(studentlist[1])
elif name == studentlist[2]:
    studentlist.remove(studentlist[2])
elif name == studentlist[3]:
    studentlist.remove(studentlist[3])
elif name == studentlist[4]:
    studentlist.remove(studentlist[4])
elif name == studentlist[5]:
    studentlist.remove(studentlist[5])
else:
    studentlist.append(name)

Reverse_studlist = studentlist.reverse()
print Reverse_studlist
print studentlist
