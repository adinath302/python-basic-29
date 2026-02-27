# ex -

from Abstraction import Shape  # from "file name" import "class name"
from math import sqrt

class Rectangle(Shape):
    def __init__(self, length, width):  # constructor
        self.length = length
        self.width = width

# implementation of abstract method is mandatory - 
    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
 # normal function non-abstract function 
    def diagonal(self):
        return sqrt((self.length) ** 2 + (self.width) ** 2)


r1 = Rectangle(100, 20)
print(r1.area())

