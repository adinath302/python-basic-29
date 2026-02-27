# oops introduction -

# seq programming -
# function programming -
# oop -

# explain - oop is a programming paradigm which is used to create objects which are used to represent real world entities
# oops is a method to orgnise the code

# class is a blueprint for creating objects
# blueprint is a template for creating objects
# blueprint does not required memory location
# class is a blueprint for creating an object it consists of attributes and methods
# class hold 2 things
# class  -> attributes(property)
#        -> methods(functions)


# syntax of class
class cls_name:
    pass
    # body


# object is an instance of a class
# it is a real world entity
# it require memory location

# syntax of object
# cls_name()
# every object has
# object -> property
#        -> action/operations

# refrence variable/object name - variable which is used to store the address of the object
#
p1 = cls_name()  # p1 is a refrence variable

# -----------------------------


class student:
    # body
    pass


amar = student()
kunal = student()
jay = student()

# print(type(amar))


class employee:
    pass


# em1 = employee()
# em2 = employee()

# print(type(em1))


class reactangle:
    pass


# rect1 = reactangle()
# rect2 = reactangle()

# inheritance -


class employee:
    pass


# e1 = employee()
# print(dir(e1))  # it will return all the attributes and methods of that class

# constructor -
# it is a special method which is used to initialize the object


class employee:
    def __new__(cls):
        print("new method is called")
        return super().__new__(cls)

    def __init__(self):  # constructor method it will be called automatically
        print("constructor is called")

    def display(self):  # method
        print("display called")


e1 = employee()  # object creation
e1.display()  # calling the method

# --------------------------------------------
# self is a refrence variable which is used to store the address of the object

class Employee1:
    def __init__(self):
        print(f"{id(self)}")


# e1 = Employee1()
# print(f"e1{id(e1)}")

# e2 = Employee1()
# print(f"e2{id(e2)}")

#-----------------------------------------------



# timeframe 1:28:00
