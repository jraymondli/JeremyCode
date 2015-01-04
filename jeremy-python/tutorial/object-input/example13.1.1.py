import sys
class Student:
    
    def __init__(self, name, courses, phone, email, credits):
        self.name = name
        self.courses = courses
        self.phone = phone
        self.email = email
        self.credits = credits
        print "Created a class instance for "+ name

    def printDetails(self):
        print "Name: ", self.name
        print "Courses: ", self.courses
        print "Phone: ", self.phone
        print "Email: ", self.email
        self.credits = len(self.courses) * 3
        print "Credit Hours: ", credits

    def enroll(self, course):
        self.courses.append(course)
class Employee:
    
    def __init__(self, Tname, age, position, subject):
        self.Tname = Tname
        self.age = age
        self.position = position
        self.subject = subject
        print "Created a class instance for "+ name

    def printDetails(self):
        print "Name: ", self.Tname
        print "Age: ", self.age
        print "Position: ", self.position
        print "Subject: ", self.subject

    def register(self, course):
        self.courses.append(course)

students = []
again = "yes"

name = ""
phone = ""
email = ""    
courses = ""
Filehandle = open('input.txt', 'r')
for line in Filehandle:
        print line
        var, val = line.split(':')
        if var == "name":
            name = val
            global name
        if var == "phone":
            phone = val
            global phone
        if var == "email":
            email = val
            global email
        if var == "courses":
            courses = val
            global courses
        if name != "" and phone != "" and email != "" and courses !="":
            print "name", name
            student = Student(name, [], phone, email, credits)
            students.append(student)
            name = ""
            phone = ""
            email = ""
            courses = ""

"""
    print "Input the courses which", student.name, "is enrolled in."
    newcourse = raw_input ("Type the course number or 'stop' ")

    while newcourse != "stop":
        student.enroll(newcourse)
        print "Input the courses which", student.name, "is enrolled in."
        newcourse = raw_input ("Type the course number or 'stop' ")

    again = raw_input ("Would you like to enter more students? ")
"""

for student in students:
    student.printDetails()

employees = []

while again != "no":
    Tname = raw_input ("Enter the teacher's name: ")
    age = raw_input ("Enter the teacher's age: ")
    position = raw_input ("Enter the teacher's position: ")
    employee = Employee(name, [], Tname, age, position)
    employee.append(employee)

    print "Input the subject which", Employee.name, "teaches."
    newcourse = raw_input ("Type the next subject or 'stop' ")

    while newcourse != "stop":
        student.enroll(newcourse)
        print "Input the subject which", student.name, "is enrolled in."
        newcourse = raw_input ("Type the next subject or 'stop' ")

    again = raw_input ("Would you like to enter more employees? ")


for employee in employees:
    employee.printDetails()
