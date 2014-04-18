class coordinates:
    positions = 0
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        coordinates.positions += 1

    def displayCount(self):
        print "Total Positions %d" % coordinates.positions

    def displayPosition(self):
        print "Coordinate : ", self.name,  ", X: ", self.x, ", Y: ", self.y

    def distance(A, B):
        x1 = A.x
        y1 = A.y
        x2 = B.x
        y2 = B.y
        d = (x1 - x2)*(x1 - x2) + (y1-y2)*(y1-y2)
        print(d**(.5))

A = coordinates("A", -1, -1)
B = coordinates("B", 1, 1)

A.displayPosition()
B.displayPosition()
print "Total Positions %d" % coordinates.positions

coordinates.distance(A,B)
