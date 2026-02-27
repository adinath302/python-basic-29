# polymorphism -

# ------------------------------------------------------------
# last session -
# >getter -
# >setter -

# ------------------------------------------------------------

# today - polymorphism - poly-many, morphism-forms
# >overloading -
# >overriding -

# ------------------------------------------------------------

# explain polymorphism - same method but diffrent action based on the object called polymorphism -

# ex 1

# name = 'raj'
# print(len(name)) # 3 char

# name = ['raj']
# print(len(name)) # 1 ele

# name = {'name': 'raj'}
# print(len(name)) # 1 key

# ex 2
# here the operator is same but the action is diffrent based on the object this is called polymorphism
# 10 + 2  # 12

# "10" + "2"  # 102

# [10] + [20]  # [10,20]

# ----------------------------------------------

# polymorphism can achive by - 2 ways

# 1. overloading - 2 types
# operator overloading -
# method overloading - 

# 2. overriding -


# ----------------------------------------------
# every data type has a class in python , inside that class there is a method and attributes -
# and the operation only work when the data type has the same method that is defined in that class -
# ----------------------------------------------

# ex 1
# n1 = 10
# n2 = 20
# print(n1 + n2)
# print(dir(n1)) # using dir you can see all the attributes and methods of that data type in python

# ex 2
# n1 =  '10'
# n2 = '20'
# print(n1 + n2)
# print(n1.__add__(n2)) # this is what happen when you use + operator

# ex 3
# s1 = {10, 20}
# s2 = {30, 40}
# print(s1 + s2)
# print(dir(s1)) # this will never work because the + operator is not defined in set

# -------------------------------------------------------
# ex - to "overload" the + operator IN class - operator overloading
# n1 = 10
# n2 = 20

# s1 = "10"
# s2 = "20"


class book:
    def __init__(self, nm, pg, pr):
        self.name = nm
        self.pages = pg
        self.price = pr

    def display(self):
        return f"""
           name     :     {self.name}
           pages    :     {self.pages}
           price    :     {self.price}
        """

    def __add__(  # overloading
        self, other
    ):  # here i overload an operator in class to perform polymorphism
        totalprice = self.price + other.price
        return book("", 0, totalprice)

    def __str__(self):  # override the default method
        return str(self.price)  # to return the price(string)


b1 = book("python programming", 200, 3000)
b2 = book("java programming", 300, 5000)
b3 = book("c programming", 150, 1000)

# print(n1 + n2)  # 30
# print(s1 + s2)  # 1020
# print(
# b1 + b2
# )  # this will never work because the + operator is not defined in book right now
print(b1 + b2 + b3)
# print(b1.display())


# -------------------------------------------------------
# ex - to "overload" the + operator IN class - operator overloading
# everytime you print and object the default method is called which is __str__

# class Student:
#     def __str__(self):
#         return print("hello")


# s1 = Student()
# print(s1)

# ----------------------------------------------------------
# ex on polymorphism(overloading) -

n1 = 10
n2 = 20

s1 = "10"
s2 = "20"


class Hotel:
    def __init__(self, nm, re):
        self.name = nm
        self.rent = re

    def rent_details(self):
        print(f"Hotel Nmme : {self.name} \n Rent per Day : {self.rent}")

    def __gt__(self, other): # operator overloading
        if self.rent > other.rent:
            return f"rent of {self.name} gt {other.name}"
        else:
            return f"No rent of {other.name} gt {self.name}"

h1 = Hotel("raj Hotel", 2000)
h2 = Hotel("taj Hotel", 3000)

print(n1 > n2)
print(s1 > s2)
print(h1 > h2)

#---------------------------------------------------------------------
# method overloading - no need to overload the method overloading because python is dynamic language