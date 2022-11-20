from math import sqrt
class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def show(self):
        print(f'Coordinates of the point are {self.a} and {self.b}')

    def move(self, a1, b1):
        self.a = a1
        self.b = b1
        print(f'New coordinates are {a1} and {b1}')

    def dist(self, a2, b2):
        self.a1 = a2
        self.b1 = b2
        print(sqrt((self.a - a2) ** 2 + (self.b - b2) ** 2))
        print(f'the difference between points {self.a-a2} and {self.b-b2}')
P = Point(int(input()), int(input()))
P.show()
P.move(int(input()), int(input()))
P.dist(int(input()), int(input()))