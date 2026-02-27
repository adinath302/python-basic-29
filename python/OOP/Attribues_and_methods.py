# class -> attributes and methods to make object

# OOPs in Python
# Two ways of programming in Python: 1) Procedural Programming,
# 2) OOPS
# OOPS: Object Oriented Programming
# A way of organizing code by creating "blueprints" (called classes) to represent real-world things like a student, car, or house. These blueprints help you create objects (individual examples of those things) and define their behavior.
# Class: A class is a blueprint or template for creating objects.
# It defines the properties (attributes) & actions/behaviors (methods) that object type will have.
# Object: An object is a specific instance of a class.
# It has actual data based on the blueprint defined by the class.

# object
# function = method -> inside class all functions becomes methods -


# self explain -  the self parameter is a refrence to the current instance(object) of the class it is used to access variables that belong to the class


class Student:  # class student
    #  __init__ is a special method which is used to initialize the value/object , constructor - fix
    # self - refrence variable / conection between class and object - fix
    def __init__(self, full_name, class_grade):  # method
        self.name = full_name  # attribute/property
        self.grade = class_grade  # attribute/property

    def student_details(self):  # method
        print(f"{self.name} is in class {self.grade}")


# student1 = Student("madhav", 11)  # object with arguments
# student2 = Student("vishakha", 12)


# student1.student_details()
# student2.student_details()

# print(student1.name, student1.grade)
# print(student2.name, student2.grade)


# ----------------------------------
class Bank:
    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:  # when amount(500) is less than balance(1000)
            self.balance -= amount
            print(f"Withdrawal successful! New balance: {self.balance}")
        else:
            print("Insufficient balance for withdrawal.")


# cus1 = Bank("rakesh", 1000)
# cus1.withdraw(500)  # method 500 = amount

# print(cus1.balance, cus1.owner_name)

# -------------------------------------


class cal_rac:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# rec1 = cal_rac(100, 50)
#
# cal_rac.area(rec1)


# ----------------------------------------------------

# Todays topic - attributes and methods

# ------------------------------------------------------
# notes - practice reading theory notes for interview

# what is object oriented programming -
# object oriented programming is a programming paradigm / way of programming / orgnizing code by using class and object

# ----------------------------------------------------

# revision -
# python paradigm - sequancial ,funcitonal ,
# first latter of class name should be capital-

# ----------------------------------------------------


class Clas_name:
    pass
    # block of code to be executed


cl1 = (
    Clas_name()
)  # object with a obeject refrence name (to store the address of the object)

# -----------------------------------------------------

# object has - properties = attributes and operations = methods
# - properties - imformation /data - if phone was object then ram , model,storage etc was properties of it .
# - operations - action /behaviour - if phone was object then call , message,email send ,gaming,clicking photos etc was operations of it

# and it is defined before creating the object inside the bluprint(class)

# -----------------------------------------------------

# 1. attributes : are variables used to store the value/data or it represent objects properties
# 3 types of attributes /variables -

# 1.instance variable
# 2.class / static variable
# 3.static variable

# ----------------------------------------------------

# 1.instance attribute -
# object level variable -
# instance attributes are defined within a constructor/method by using self keyword
# it create separate copy of the attribute for each object
# instance attributes are diffrent for each obejct that's why you can not access it through class name

# example -
# class Cls_name:
#     def __init__(self):
#   self.ia = value - instance attribute

# ----------------------------------------------------

# 2.class/static attribute -
# class level (data) -
# explain class level - value of an data which is same for all objects of a class
# which is define outside the constructor/method inside of the class
# it only create one copy of the attribute for the class
# we can access class attributes by using class name or object refrence variable

# ex :
# class Cls_name:
#     ia = value  # class attribute
#
#     def __init__(self):
#        self.ia = value - instance attribute


# ---------------------------------------------------


# 3.Local attribute -
# method level -
# explain local attribute -   value defined wihin a method inside the class
# ex
# class Cls_name:
#     ia = value  # class attribute
#
#     def __init__(self):
#        self.ia = value - instance attribute
#
#    def method_name(self):
# self.ia = value -#      local attribute

# ----------------------------------------------------


class Student:
    institute = "ABC"  # class attribute
    course = "python"
    trainer = "vishakha"

    def __init__(self, rl, nm, ag, mk):
        self.roll = rl  # instance attribute
        self.name = nm
        self.age = ag
        self.marks = mk  # this called initialization of instance variable/attributes

    def grade(self):
        grade = "hello"  # local attribute


s1 = Student(1, "om", 23, 200)
s2 = Student(2, "raj", 13, 20)

# to access instance attribute outside the class - by using object refrence variable

print(s1.name)
print(s1.age)
print(s1.marks)

# to access class attributes outside the class - by using class name
print(Student.course)
print(Student.trainer)
print(Student.institute)

# to access class attributes outside the class - by using object refrence variable
print(s1.institute)
print(s1.trainer)
print(s2.course)
# ----------------------------------------------------
# employee


class employee:
    company = "abc" # class attributes
    working_hour = "8 hours"

    def __init__(self, na, sal, exp): # constructor
        self.name = na
        self.salary = sal
        self.experience = exp

    def display(self): # method
        print(self.name) # local attribute
        print(self.salary)
        print(self.experience)
        print(self.company)
        print(self.working_hour)


e1 = employee('om',10000,2)

# ----------------------------------------------------
# phone -

class phone:
    company ="vivo"  # class attribute
    
    def __init__(self):
        self.color = 'black' # instance attribute
        self.model = "vivo_y12"
        self.ram = "4gb"
        self.storage = "64gb"
    
    def display(self):
        print(f'')
# ----------------------------------------------------
# ----------------------------------------------------
# pass - it act as a placeholder for a statement but where you, the programmer, don't want any code to run


# timeframe - 1:19:07
