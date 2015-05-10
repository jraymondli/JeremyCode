b = [] 

while True:
    try:
        a = raw_input()
        print a
        b.append(a)
    except EOFError:
        break


