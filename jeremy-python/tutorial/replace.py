FH1 = open('A', 'r')
FH2 = open('B', 'w')

for line in FH1:
    line = line.strip('\n')                                
    print >> FH2, line
    print line, 'A'
