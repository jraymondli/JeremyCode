##############################################################################
# This program takes an input and then aligns it by center and also surrounds 
# it with astericks.
# Author: Jeremy Li
# May 9, 2015
##############################################################################
 
b = []
e = 0
f = 0
i = 0
j = 0
g = 0
l = 0
while True:
    try:                                                     
        a = raw_input()
	b.append(a)
    except EOFError:
        break
c = len(b)-1
while e <= c: 
    if f < len(b[e]):
      f = len(b[e]) 
      e = e+1
    else:
      e = e + 1
print '*' * (f+2)
g = 0
for x in range(len(b)):
   h  = len(b[g])
   i = f - h
   if i == 0:
      print ''.join(str(y) for y in ('*',b[g],'*'))
   elif i/2 * 2 != i:
      if l == 0:
          j = (i-1)/2
          k = (i+1)/2
          print ''.join(str(y) for y in ('*',' ' * j,b[g],' ' * k,'*'))
          l = 1
      else:
         j = (i-1)/2
         k = (i+1)/2
         print ''.join(str(y) for y in ('*',' ' * k,b[g],' ' * j,'*'))
         l = 0
   else:
       j = i/2 
       print ''.join(str(y) for y in ('*',' ' * j,b[g],' ' * j,'*'))  
   g = g + 1
print '*' * (f+2)
