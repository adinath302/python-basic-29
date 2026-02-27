# today
# functional programming
# > functions
# > parameter and arguments

# ----------------------------

# functional programming - function is a reusable block of code it is used to perform operations on data
# parameter - is a variable that is defined in the function definition
# arguments - is the value that is passed to the function when it is called

# ---------------------------

# python support 3 main programming paradigms - these are the ways to structure and orgnise the code

# 1. sequential programming(it's done)  - step by step execution of code but you can't reuse the code
# 2. functional programming - function is a block of code that can be reused
# 3. object-oriented programming -

# ---------------------------

# 1 - functinal programming -
# function - is a reusable block of code that operations on data
# create a reusable block of code that can be called in multiple places in the program
# syntax -
# it will never execated because there is no function call
# to call the function - function_name() - 'function name()"

# def function_name(parameters):
#      code'
#      body

# normal function
# num = int(input("enter a number - "))
# squ = num**2
# print(squ)

# reusable function code
# def square():
#     num = int(input("enter a number - "))
#     squ = num**2
#     print(squ)

# def isperfect(): # reusable function to check perfect number inside a block
#     num = int(input("enter a number - "))
#     sum = 0  # sum of i (which are divisible by num)
#     for i in range(1, num): # iterate the numbers from 1 to num to apply logic in it
#         if num % i == 0: # if the reminder is 0
#             sum = sum + i
#     if sum == num:
#         print(f"{num} is a perfect number")
#     else:
#         print(f"{num} is not a perfect number")

# ex  1

# def get_data():
#     name=input("enter your name - ")
#     print(f'hello, {name}')

# # function call
# get_data()

# -----------------------------
# sequential programming -  this code is not reusable
# num = int(input("enter a number - "))
# cu = num**3
# print(cu)

# -----------------------------
# functional programming - reusable code block
# this code can't run without function call
# def cube():
#     num = int(input("enter a number - "))
#     cu = num**3
#     print(cu)

# cube()  # function call - needed to execute the function code

# -----------------------------
#
# cube() # then you can call it multiple times to reuse the code(no need to rewrite the code again and again)

# --------------------------------
# create a function to check is number is odd or not
# create a function to check is negative or not
# create a function to check mobail number is valid or not


# --------------------------------
# odd or not -
def is_odd():
    no = int(input("enter a num - "))
    if no % 2 == 1:
        print(f"{no} is odd number")
    else:
        print(f"{no} is not an odd number")


# is_odd() # function calling


# --------------------------------
# negative or not -

# def is_nagative():
#     num = int(input('enter a num - '))
#     if num < 0:
#         print(f'{num} is a negative number')
#     else:
#         print(f"{num} is a positive number")


# is_nagative()
# is_nagative()


# ----------------------------------
# mobail no is valid or not
def is_valid_mobail():
    number = input("enter mobail no - ")
    if len(number) == 10 and number.isnumeric():
        print(f"{number} is valid")
    else:
        print(f"{number} is NOT valid")


# is_valid_mobail()  # function calling is important to execute the code


# ----------------------------------
# parameter and arguments -


def sum(a, b):  # a and b are parameters
    res = a + b
    print(res)


# sum(5, 7)  # 5 and 7 are - arguments

# --------------------------------


def greet(name):  # parameter
    print(f" hello {name}")


# greet("Alice")  # argument

# ----------------------------------
# wap to print full name


def full_name(first, middle, last):
    print(f"{first} {middle} {last}")


# full_name("yashwant", "hambirrao", "jadhav")  # arguments

# ---------------------------------
# caf to calculate simple interest


def simple_int(p, r, t):
    res = p * (r / 100) * t
    print(res)


#  principal, rate, time
# simple_int(10000, 5, 3)


# ----------------------------------
# wap to calculate percentage
def percentage(part, total):
    res = (part / total) * 100
    print(res)


# percentage(50,100)

# ----------------------------------


# cf to check student pass or fail
def is_pass(marks, pass_mark):
    if marks > pass_mark:
        print("pass")
    else:
        print("fail")


# is_pass(68,35)

# ---------------------------------------
# grade of student

def stu_grade(mar):
    if mar > 90:
        print("A+")
    elif mar > 80:
        print("A")
    elif mar > 70:
        print("B+")
    elif mar > 60:
        print("B")
    else:
        print("C")


# timeframe 1:25:15

# python notes :------

# ----------------------------------

# an input allways return a str(string) data type
# and len() only works on list string collection of data not on

# ----------------------------------
# module -
# module is a python file that contains functions , class and variables

# ----------------------------------
# to import a module -

# import (keyword) module name(anything after import is module name)

# import introduction.py # example

# ----------------------------------
# pass - if you don't want to write any code inside the function you can use pass keyword
