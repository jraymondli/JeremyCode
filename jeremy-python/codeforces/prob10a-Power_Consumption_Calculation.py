##################################################
# http://codeforces.com/problemset/problem/10/A
# Progam that determines power consumption given:
# power consumed:on, screensaver, sleep
# time before:screensaver, sleep
# work periods
##################################################
inputs = raw_input().split(' ')
shutdownTimes = []
times = []
energy = 0
while True:
    try:
        times.append(raw_input().split(' '))
    except EOFError:
        break
n = int(inputs[0])
P1 = int(inputs[1])
P2 = int(inputs[2])
P3 = int(inputs[3])
T1 = int(inputs[4])
T2 = int(inputs[5])
##################################################
# Above takes all input and sorts it
##################################################
counter = 0
for x in range(n):
    energy = energy + int(P1*(int(times[counter][1])-int(times[counter][0])))
    counter = counter + 1
##################################################
# energy consumed during use of device
##################################################
counter = 0
for x in range(n-1):
    counter = int(times[x + 1][0])-int(times[x][1])
    if T1 >= counter:
        energy = energy + counter*P1
    else:
        energy = energy + T1*P1
        if T2+T1 >= counter:
            energy = energy + (counter-T1)*P2
        else:
            energy = energy + T2*P2
            energy = energy + (counter - (T1+T2))*P3
##################################################
# Energy consumed during screensaver&sleep mode
##################################################
print energy

