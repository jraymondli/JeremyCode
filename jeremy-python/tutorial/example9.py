counter = 0
guesses = 1
print "Type in the", guesses ,"number"
counter + 1
answer = raw_input("Try to guess the lucky number!")
while counter <= 5:
    print "Type in the", guesses + 1, "number"
    counter = counter + 1
    if counter == 5:
        print "You didn't guess the answer"
        quit()
    if answer != '1':
        guesses = guesses + 1
        print "That is not the right number!"
        answer = raw_input("Try to guess the lucky number!")
    else:
        print counter
        print "You guessed",guesses, "times"
        break

