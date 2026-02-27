# today's topic -
# Abstraction -
# comprehension -

# --------------------------------------
# abstraction -
# explain - Abstraction in Python is a fundamental principle of object-oriented programming (OOP) that involves hiding the complex implementation details and showing only the necessary features to the user.It allows developers to focus on what an object does rather than how it does it, simplifying code, improving readability, and promoting code reusability
# to show only nesessary features to the user
# Why do we need Abstraction? -
# - It simplifies the interface for users.
# - It reduces the complexity of the code.
# - It makes the code more maintainable and reusable.

# abstract method -
# no object and logic inside of abstract class
# in abstract method it does not have any declaration of body
# in abstract class can have non-abstract(normal) methods and abstract methods both
# it is mendatory to implement all the methods of abstact(parent) class in child class
# if a class have all abstract methods it called as interface class and a class have both (normal and abstract method) is called as abstract class

# Abstract class
from abc import ABC, abstractmethod


class Cls_name(ABC):
    @abstractmethod  # Decorator
    def m1(self):
        pass


# --------------------------------------
# ex

from abc import ABC, abstractmethod


class Shape(  # it's an abstract class
    ABC
):  # you have to inherit the non-abstract by "ABC" to create a abstract class *
    @abstractmethod  # decorator to define abstract method *
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def welcome(self):
        print("welcome to shape")
        

obj1 = Shape()

# -------------------------------------
# # ex -

# class Rectangle:
#     def __init__(self,length,width): # constructor
#         self.length = length
#         self.width = width

# r1 = Rectangle(100,20)

# --------------------------------------
# --------------------------------------
# --------------------------------------
# --------------------------------------
# --------------------------------------
# --------------------------------------


# timeframe 32:10
