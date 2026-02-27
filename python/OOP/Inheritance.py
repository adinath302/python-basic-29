# 1)What is Inheritance in Python?
# Inheritance is one of the fundamental concepts in Object-Oriented Programming (OOP). It allows a class (called a child class or subclass) to inherit properties(attributes) and methods from another class (called a parent class or superclass). 

# Inheritance allows for code reuse and establishes a relationship between the parent and child classes. The child class can use the functionalities of the parent class and also add its own unique behaviors.

# 2)what are Key Features of Inheritance?
# Code Reusability:
# The child class can inherit methods and properties from the parent class, reducing the need to rewrite common functionality.

# Extensibility:
# The child class can add or override methods and properties to extend or customize the behavior of the parent class.

# Method Overriding:
# The child class can override methods of the parent class to provide a more specific implementation.

# Hierarchical Relationship:
# Inheritance establishes a relationship where the child class is a more specific version of the parent class.

# 3)what are types of Inheritance??
# Types of Inheritance in Python
# a)Single Inheritance:
# ----------------------
# Where A subclass inherits from one parent class.
# eg.
# Parent Class -
class Device:
    def __init__(self, brand):
        self.brand = brand

    def display_info(self):
        print(f"Device Brand: {self.brand}")

# Child Class
class Smartphone(Device):
    def __init__(self, brand, model):
        super().__init__(brand)  # Call parent class constructor for brand attribute
        self.model = model

    def display_model(self):
        print(f"Smartphone Model: {self.model}")

# Usage
# smartphone = Smartphone("Apple", "iPhone 15")
# smartphone.display_info()  # Device Brand: Apple
# smartphone.display_model()  # Smartphone Model: iPhone 15

# b)Multiple Inheritance :
# ---------------------
# In Multiple Inheritance, a subclass inherits from more than one parent class. The child class can inherit properties and methods from multiple classes.
# eg.
# Parent Class 1
class Device:
    def __init__(self, brand):
        self.brand = brand

    def display_info(self):
        print(f"Device Brand: {self.brand}")

# Parent Class 2
class Features:
    def __init__(self, color, storage):
        self.color = color
        self.storage = storage

    def display_features(self):
        print(f"Color: {self.color}, Storage: {self.storage}")

# Child Class
class Smartphone(Device, Features): # Multiple Inheritance
    def __init__(self, brand, color, storage, model):
        Device.__init__(self, brand)  # Initialize parent Device class
        Features.__init__(self, color, storage)  # Initialize parent Features class
        self.model = model

    def display_model(self):
        print(f"Smartphone Model: {self.model}")

# Usage
# smartphone = Smartphone("Apple", "Black", "128GB", "iPhone 15")
# smartphone.display_info()  # Device Brand: Apple
# smartphone.display_features()  # Color: Black, Storage: 128GB
# smartphone.display_model()  # Smartphone Model: iPhone 15

# c)Multilevel Inheritance
# ---------------------------
# In Multilevel Inheritance, a subclass inherits from a class, and that class inherits from another class, forming a multi-level chain.
# eg.
# Parent Class
class Device:
    def __init__(self, brand):
        self.brand = brand

    def display_info(self):
        print(f"Device Brand: {self.brand}")

# Child Class (Inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model):
        super().__init__(brand) # super is used to call parent class constructor
        self.model = model

    def display_model(self):
        print(f"Smartphone Model: {self.model}")

# Grandchild Class (Inherits from Smartphone)
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, camera_resolution):
        super().__init__(brand, model)
        self.camera_resolution = camera_resolution

    def display_camera(self):
        print(f"Camera Resolution: {self.camera_resolution}MP")

# Usage
# smartphone = SmartphoneWithCamera("Apple", "iPhone 15", 48)
# smartphone.display_info()  # Device Brand: Apple
# smartphone.display_model()  # Smartphone Model: iPhone 15
# smartphone.display_camera()  # Camera Resolution: 48MP

# d)Hierarchical Inheritance
# ----------------------------
# In Hierarchical Inheritance, multiple subclasses inherit from a single parent class. This type of inheritance allows you to create different types of objects from a single base class.
# eg.
# Parent Class
class Device:
    def __init__(self, brand):
        self.brand = brand

    def display_info(self):
        print(f"Device Brand: {self.brand}")

# Child Class 1
class Smartphone(Device):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display_model(self):
        print(f"Smartphone Model: {self.model}")

# Child Class 2
class Laptop(Device):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display_model(self):
        print(f"Laptop Model: {self.model}")

# Usage
# smartphone = Smartphone("Apple", "iPhone 15")
# laptop = Laptop("Dell", "XPS 13")

# smartphone.display_info()  # Device Brand: Apple
# smartphone.display_model()  # Smartphone Model: iPhone 15

# laptop.display_info()  # Device Brand: Dell
# laptop.display_model()  # Laptop Model: XPS 13

# e)Hybrid Inheritance
# Hybrid Inheritance is a combination of two or more types of inheritance. It involves multiple inheritance, multilevel inheritance, and hierarchical inheritance all at once.

# 4)What is Method Resolution Order (MRO), and how does it work in Python inheritance?
# Answer:
# MRO determines the order in which Python looks for a method in a hierarchy of classes when a method is called. Python follows the C3 linearization algorithm to determine this order.

# You can view the MRO of a class using the ClassName.mro() or ClassName.__mro__ attribute.
# eg.
class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):  # Multiple inheritance
    pass

d = D()
d.show()  # Output: Class B
print(D.mro())  # [D, B, C, A, object]
# Explanation:
# When d.show() is called, Python checks the method in the order [D, B, C, A] and executes the first one it finds, which is Class B.

# 5)How can you access a method from a parent class if it is overridden in a child class?
# Answer:
# You can explicitly call the parent classâ€™s method using the class name or super().

# 6)Can a child class override the parent classâ€™s __init__ method? How do you handle it if you still need to initialize the parent class?
# Answer:
# Yes, the child class can override the __init__ method. To still initialize the parent class, use super().__init__().

# 7)What is the difference between overriding and overloading in the context of inheritance in Python? Does Python support overloading?
# Answer:
# Overriding: A subclass provides a specific implementation of a method already defined in the parent class.
# Overloading: Providing multiple methods in the same class with the same name but different arguments.
# Python does not directly support overloading

# 8)What happens if two parent classes define a method with the same name and a child class inherits from both?
# Answer:
# The method from the parent that appears first in the MRO is called.

# 9)How can you restrict a class so that it cannot be inherited?
# Answer:
# To prevent inheritance, use the final decorator from the typing module (Python 3.8+).

# eg.
from typing import final
@final
class Device:
    pass

class Smartphone(Device):  # Error: Cannot inherit from	final class
    pass

# ===================ThankYou=======================
# VaibhavPatil
# PythonTrainer
# TheKiranAcademy
# Karve Nagar Pune


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

from datetime import date
class Saving_account:
    #properties -> ATTRIBUTES
    #->class level
    bank_name = 'Bank Of Maharashtra'
    branch = 'Karve Nagar'
    ifsc_code = 'BOM10134'
    def __init__(self,nm,ac,bal):
        #object level
        self.name = nm
        self.account = ac
        self.balance = bal
        self.transaction = {}
        
    #operations ->methods
    def check_balance(self):
        print(f'Balance : {self.balance}')

    def add_transaction(self,date,type,amount,balance):
        self.transaction[len(self.transaction)+1] = {'date':date,'type':type,'amount':amount,'balance':balance}
        return 'done'
        
    
    def deposit(self,amount):
        if isinstance(amount,(int,float)):
            if amount>0:
                self.balance = self.balance+amount
                dt = date.today()
                bal =  self.balance
                self.add_transaction(dt,'deposit',amount,bal)
                return f'xxxxx{str(self.account)[-3:]} credited by {amount} on {dt} Avl {bal}'
            else:
                return 'please enter positive value only'
        else:
            return 'please enter numeric value only'
    def withdraw(self,amount):
        if isinstance(amount,(int,float)):
            if amount>0:
                self.balance = self.balance-amount
                dt= date.today()
                bal =self.balance
                self.add_transaction(dt,'withdraw',amount,bal)
                return f'xxxxx{str(self.account)[-3:]} debited by {amount} on {dt} Avl {bal}'
            else:
                return 'please enter positive value only'
        else:
            return 'please enter numeric value only'
        
    def show_transaction(self):
        print('-'*106)
        print(f'|{'Sr.':^20}|{'Date':^20}|{'Type':^20}|{'Amount':^20}|{'Balance':^20}|')
        print('-'*106)
        for sr in self.transaction:
            print(f'|{sr:^20}|{str(self.transaction[sr]['date']):^20}|{self.transaction[sr]['type']:^20}|{self.transaction[sr]['amount']:^20}|{self.transaction[sr]['balance']:^20}|')
            print('-'*106)

# sa1 = Saving_account('kunal kale',123456101,20000)
# sa2 = Saving_account('Rahul Jadhav',123456102,10000)
# sa3 = Saving_account('Pavan Raut',123456103,50000)
# sa1.check_balance()
# print(sa1.deposit(10000))
# print(sa1.withdraw(5000))
# print(sa1.deposit(40000))
# sa1.show_transaction()


#================================================================




