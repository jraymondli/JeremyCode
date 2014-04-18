answer = raw_input("Try to guess the lucky number!")
while answer != '1':
    print "That is not the right number!"
    question =  raw_input('Do you want to try again?')
    if question == 'yes': 
        answer = raw_input("Try to guess the lucky number!")
    else:
        print('all right.')
        quit()
else:
    print "You guessed it!!"

