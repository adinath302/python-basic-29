# ex

from Abstraction import Shape


class Square(Shape):  # after inheritance the square class is a child class
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4*self.side
