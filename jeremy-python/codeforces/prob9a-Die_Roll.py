input = raw_input().split(' ')
if input[0] > input[1]:
    top = input[0]
else:
    top = input[1]
No = 7 - int(top)
divis = '/'
if No == 2:
    fraction = str(No/2) + divis + '3'
    print fraction
elif No == 3:
    fraction = str(No/3) + divis + '2'
    print fraction
elif No == 4:
    fraction = str(No/2) + divis + '3'
    print fraction
elif No == 6:
    fraction = str(No/6) + divis + '1'
    print fraction
else:
    fraction = str(No) + divis + '6'
    print fraction
