# encapsulation -
# explain 1 - Encapsulation in Python is the process of bundling data (attributes) and the methods that operate on that data into a single unit, usually a class. It restricts direct access to internal components to prevent accidental modification and data corruption.
# explain 2 - Encapsulation means hiding internal details of a class and only exposing what’s necessary. It helps to protect important data from being changed directly and keeps the code secure and organized.

# Why do we need Encapsulation?
# Protects data from unauthorized access and accidental modification.
# Controls data updates using getter/setter methods with validation.
# Enhances modularity by hiding internal implementation details.
# Simplifies maintenance through centralized data handling logic.
# Reflects real-world scenarios like restricting direct access to a bank account balance.

# access specifiers 3 - 

# encapsulation - it is the process of binding data and methods together into a single unit.
# getter method is used to access private attribute 
# setter method is used to update private attribute


# public - no prefix - Public members are variables or methods that can be accessed from anywhere inside the class, outside the class or from other modules. By default, all members in Python are public. They are defined without any underscore prefix (e.g., self.name).
# ex 
class Employee:
    def __init__(self, name):
        self.name = name   # public attribute

    def display_name(self):   # public method
        print(self.name)

emp = Employee("John")
emp.display_name()   # Accessible
print(emp.name)      # Accessible

# private - __ double underscore - Private members are variables or methods that cannot be accessed directly from outside the class. They are used to restrict  . In Python, private members are defined with a double underscore prefix (e.g., self.__salary). Python applies name mangling by internally renaming them (e.g., __salary becomes _ClassName__salary) to prevent direct access.
# ex - 
class Employee:
    def __init__(self, name, salary):
        self.name = name          # public
        self.__salary = salary    # private

    def show_salary(self):
        print("Salary:", self.__salary)

emp = Employee("Robert", 60000)
print(emp.name)          # Public accessible
emp.show_salary()        # Accessing private correctly
# print(emp.__salary)    # Error: Not accessible directly

# protected - _ single underscore - Protected members are variables or methods that are intended to be accessed only within the class and its subclasses. They are not strictly private but should be treated as internal. In Python, protected members are defined with a single underscore prefix (e.g., self._name).
# example - 
class Employee:
    def __init__(self, name, age):
        self.name = name       # public
        self._age = age        # protected

class SubEmployee(Employee):
    def show_age(self):
        print("Age:", self._age)   # Accessible in subclass

emp = SubEmployee("Ross", 30)
print(emp.name)        # Public accessible
emp.show_age()         # Protected accessed through subclass

# ----------------------------------------
# Bank Account -

class Bank_accout:
    def __init__(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            return "invalid number"

    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount
            return self.__balance
        else:
            return "invalid number"

    def withdraw(self, get_amount):
        if get_amount > 0 and get_amount <= self.__balance:
            self.__balance = self.__balance - get_amount
            return self.__balance
        else:
            return "invalid number or amount"

    def get_balance(self):
        return f"the current balance is {self.__balance}"
    
    def __str__(self):
        return f"the current balance is {self.__balance:.2f}"

c1 = Bank_accout(1000)

# Getter and Setter Methods - 
# In Python, getter and setter methods are used to access and modify private attributes safely. Instead of accessing private data directly, these methods provide controlled access, allowing you to:

# you can get private data using getter methods
# and set/updata data using setter methods in pytho class 
# ex -
class Employee:
    def __init__(self):
        self.__salary = 50000  # Private attribute

    def get_salary(self):    # Getter method
        return self.__salary

    def set_salary(self, amount):   # Setter method
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary amount!")

emp = Employee()
print(emp.get_salary())  # Access salary using getter

emp.set_salary(60000)   # Update salary using setter
print(emp.get_salary())

# Explanation:

# __salary is a private attribute, so it can't be accessed directly from outside the class.
# get_salary() is a getter method that safely returns the current salary.
# set_salary(amount) is a setter method that updates the salary only if the amount is positive.
# The object emp uses these methods to access and modify the salary while keeping the data protected.