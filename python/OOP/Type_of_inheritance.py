# Parent Class
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited successfully.")

    def show_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: {self.balance}")


# Child Class (Inheritance)
class SavingsAccount(BankAccount):

    def add_interest(self, interest_rate):
        interest = self.balance * interest_rate / 100
        self.balance += interest
        print(f"Interest of {interest} added.")


# Creating Object of Child Class
acc1 = SavingsAccount("Vaibhav", 10000)

acc1.show_balance()  # Inherited method
acc1.deposit(2000)  # Inherited method
acc1.add_interest(5)  # Child class method
acc1.show_balance()


# multiple
# Parent Class 1
class Employee:

    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def show_details(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.emp_id)


# Parent Class 2
class Salary:

    def calculate_salary(self, basic):
        hra = basic * 0.20
        da = basic * 0.10
        total = basic + hra + da
        return total


# Child Class (Multiple Inheritance)
class Manager(Employee, Salary):

    def show_full_info(self, basic_salary):
        self.show_details()  # inherited method From Employee
        total_salary = self.calculate_salary(basic_salary)  # From Salary
        print("Total Salary:", total_salary)


# Creating Object
m1 = Manager("Vaibhav", 101)

m1.show_full_info(50000)


# multilevel inheritance
# Level 1 - User (Basic Information)
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def login(self):
        print(f"{self.username} logged in successfully.")


# Level 2 - Customer (Inherits User)
class Customer(User):

    def __init__(self, username, email, cart_value):
        super().__init__(username, email)
        self.cart_value = cart_value

    def place_order(self):
        print(f"Order placed successfully. Cart Value: {self.cart_value}")


# Level 3 - PrimeCustomer (Inherits Customer)
class PrimeCustomer(Customer):

    def apply_discount(self):
        discount = self.cart_value * 0.10
        final_amount = self.cart_value - discount
        print(f"Prime Discount Applied: {discount}")
        print(f"Final Amount to Pay: {final_amount}")


# Creating Object
p1 = PrimeCustomer("Vaibhav", "vaibhav@gmail.com", 5000)

# p1.login()  # From User
# p1.place_order()  # From Customer
# p1.apply_discount()  # From PrimeCustomer


# Hierarchical Inheritance
# Parent Class
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def show_details(self):
        print("Employee Name:", self.name)
        print("Base Salary:", self.base_salary)


# Child Class 1
class Developer(Employee):

    def calculate_salary(self, projects_completed):
        bonus = projects_completed * 3000
        total_salary = self.base_salary + bonus
        print("Developer Final Salary:", total_salary)


# Child Class 2
class Manager(Employee):

    def calculate_salary(self, team_size):
        bonus = team_size * 2000
        total_salary = self.base_salary + bonus
        print("Manager Final Salary:", total_salary)


# Creating Objects
dev1 = Developer("Vaibhav", 40000)  # it's name and base salary for developer
dev1.show_details()
dev1.calculate_salary(3)

print("---------------")

mgr1 = Manager("Rahul", 60000)
mgr1.show_details()
mgr1.calculate_salary(5)

# ----------------------------------------------------


# ex 1 -
# multiple inheritance
class p1:
    def m1():
        print("m1 method from p1 class")

    def m2():
        print("m2 method from p1 class")


class p2(p1):
    def m3():
        print("m1 method from p1 class")

    def m4():
        print("m2 method from p1 class")


class p3(p2):
    def m5():
        print("m1 method from p1 class")

    def m6():
        print("m2 method from p1 class")


class c(p3):
    pass

f1 = c

# f1.m1()  # from here i can access all the methods of p1 class and p2 class and p3 class because of multilevel inheritance

# --------------------------------------------------
# ex  2 inheritance - the vehicle starter

class Vehicle:
    def drive():
        print('the vehicle is moving ')

class Car(Vehicle):
    pass

c1 = Car()
c1.drive()

#--------------------------------------------------
# ex 3

#--------------------------------------------------