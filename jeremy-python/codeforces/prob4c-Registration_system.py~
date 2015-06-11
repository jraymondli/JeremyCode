# NOTE: THIS ONLY WORKS FOR TESTS 1-6.
##############################################################################
# This is code for a registration system. First it is given a username. Then it
# checks if there has been a copy. If there is, it checks the username with the
# highest number and then adds one. Then it registers the username and keeps 
# registering until it is done.
##############################################################################
a = input()
b = []
##############################################################################
# a is the nuber of rounds that were played
# b is the list to store those rounds
# Next is if and else statements to check if users can be added. 
##############################################################################
for x in range(a):
    c = raw_input()
    f = c in b
    if f == False:
       b.append(c)
       print"OK"
       ########################################################################
       # The above checks for wether there is a repetition in the usernames
       # or not.
       # If there is none, it adds the name, if there isn't it continues.
       # Problem url: http://codeforces.com/problemset/problem/4/C
       ########################################################################
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
