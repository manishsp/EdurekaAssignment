# A Robot moves in a Plane starting from the origin point (0,0). The robot can move
# toward UP, DOWN, LEFT, RIGHT. The trace of Robot movement is as given
# following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# The numbers after directions are steps. Write a program to compute the
# distance current position after sequence of movements.
# Hint: Use math module.

# As per my understanding, the question is about the Eucliedean Distance
# From above details, the co-ordinates derived on graph are P=(x1,y1) i.e P=(0,0) and Q=(x2,y2)) i.e Q=(-1,2)
# formula is d=squareroot(square(x2-x1)+ square(y2-y1); So solving this assignment on this assumption

import math

class EuclideanDistance:

    def __init__(self, x2, x1, y2, y1):
        self.x2 = x2
        self.x1 = x1
        self.y2 = y2
        self.y1 = y1

    def EucDis(self):
        return math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)


eucd = EuclideanDistance(-1, 0, 2, 0)
print(eucd.EucDis())
