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
           
           while g == True:
              z = -1
              z = z-1
              g = c[z:] == int
           h = int(c[z:])
           h = h + 1
           c[:z]
           ''.join(str(x) for x in (c,h))
           b.append(c)
           print c

