##############################################################################
# This is code for a registration system. First it is given a username. Then it
# checks if there has been a copy. If there is, it checks the username with the
# highest number and then adds one. Then it registers the username and keeps 
# registering until it is done.
##############################################################################
a = input()
b = []
for x in range(a):
    c = raw_input()
    f = c in b
    if f == False:
       b.append(c)
       print"OK"
    else:
       e = c[-1:]
       g = e == int
       if g == False:
           c = ''.join(str(x) for x in (c,1))
           f = c in b
           if f == True:
               h = 1
               while f == True:
                  c = c[:-1]
                  c = ''.join(str(x) for x in (c,h))
                  f = c in b
                  if f == True:
                      h = h + 1
                  else:
                      print c
                      b.append(c)
           else:
               print c
               b.append(c)
       else:  
           g == True
           while g == True:
              z = -1
              try:
                 int(g)
              except ValueError:
                 z = z-1
                 g = c[z:]
           h = int(c[z:])
           h = h + 1
           c[:z]
           ''.join(str(x) for x in (c,h))
           b.append(c)
           print c

