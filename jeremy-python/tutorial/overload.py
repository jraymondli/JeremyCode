class Vector:
   def __init__(self, a, b, c):
      self.a = a
      self.b = b
      self.c = c
      
   def __str__(self):
      return 'Vector (%d, %d, %d)' % (self.a, self.b, self.c)
   
   def __mul__(self,other):
      return(self.a * other.a + self.b * other.b + self.c * other.c)

v1 = Vector(1,2,3)
v2 = Vector(3,2,1)
print v1 * v2
