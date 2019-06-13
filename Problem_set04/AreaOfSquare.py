class Shape:

    def __init__(self):
        pass

    def area(self):
        self.a = 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        print self.length ** 2


square = Square(5)
square.area()
