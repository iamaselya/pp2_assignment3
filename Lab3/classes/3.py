class Shape:
    def __init__(self):
        pass

    def area1(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area2(self):
        return self.length*self.width

A = Rectangle(int(input()), int(input()))
print(A.area2())