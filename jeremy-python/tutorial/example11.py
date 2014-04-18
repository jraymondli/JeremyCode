#1.1) Create a list that contains the names of 5 students of this class. (Do not ask for input to do that, simply create the list.) Print the list. Ask the user to input one more name and append it to th#e list. Print the list. Ask a user to input a number. Print the name that has that number as index. Add "John Smith" and "Mary Miller" at the beginning of the list (by using "+"). Print the list.
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
