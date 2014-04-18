import sys
import urllib2

if len(sys.argv) < 3:
    print("Input more parameters")
    quit()
else:
    print sys.argv[1]
    print ('transfered to')
    print sys.argv[2]

FileHandle1 = open(sys.argv[1],'r')
FileHandle2 = open(sys.argv[2],'w')
                        
for line in FileHandle1:
    print >> FileHandle2, line.strip()

