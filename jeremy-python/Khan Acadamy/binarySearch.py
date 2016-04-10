array = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
print"Please input a number from 1-100. I will tell you whether it is prime or not, and also it's index if it is prime."
value = input()
counter = 0
min = 0
max = len(array)-1
guess = (min + max)/2

while array[guess] != value and counter < 7:
    guess = (min + max)/2
    if array[guess] > value:
        max = guess
    if array[guess] < value:
        min = guess
    counter += 1

if array[guess] == value:                                                                                                                                            
    print"your number is a prime, and it is prime number %s." % str(int(guess)+1)
else:
    print "your number is not a prime."
