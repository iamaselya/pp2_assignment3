class Shape:
    def __init__(self):
        pass

    def area1(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area2(self):
        return self.length**2

A1 = Shape()
A2 = Square(int(input()))
print(A1.area1(), A2.area2())