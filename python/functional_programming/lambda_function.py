# lambda function -

# --------------------------------------
# lamda function -
# explain - it is a single line function used for performe simple operations
# lambda - keyword
# nameless function (anonymous function) but you can assign it to a variable after assigning it a variable it was not a nameless function then it was a normal function
# no need to write return statement it return automaticaly
# diffrence between normal and lambda function - normal function is used to perform complex operations and lambda function is used to perform simple operations
# syntax :
# lambda parameter : expression(logical statement)
# we can write multiple expressions in lambda function by using tuple

# higher order function (HOF) -
# explain - a function which take another function as a argument or return a function as result called as higher order function
# python has inbuild higher order functions - 1. map 2. filter 3. reduce

# filter -
# explain - 
#  filter always return true or false it takes two arguments 1. function 2. iterable

# --------------------------------------
# diffrence between normal and lambda function -
#  normal                                            lambda function
# def square(num):                                 print((lambda num : num**2)(4))
#     return num**2

# square(4)
# --------------------------------------

# addition -  using lambda function

# print((lambda n1, n2: n1 + n2)(10, 20))

# -------------------------------------
# using lambda function - you can assign it to a variable

is_divisible = (lambda n1, n2: n1 % n2 == 0)(10, 2)  # true
# print(is_divisible)
# -------------------------------------
# wap to check number is divisible by 3 and 5

is_divisible1 = (lambda n2: n2 % 3 == 0 and n2 % 5 == 0)(12)
# print(is_divisible1)

# -------------------------------------
# create a lambda function to return full name

full_name = (lambda first, middle, last: f"{first} {middle} {last}".title)(
    "ajay", "kaituk", "parakhe"
)
# print(full_name)
# -------------------------------------
# create a single lambda function to return add,sub,mul,division of 2 numbers
# you can write multiple expressions in lambda function by using tuple
is_solve = (lambda f1, f2: (f1 + f2, f1 - f2, f1 * f2, f1 / f2))(2, 3)
# print(is_solve)

# -------------------------------------
# trying all types of argument
# -------------------------------------

# add -  positional argument

add = lambda n1, n2: n1 + n2

# print(add(2, 3))

# -------------------------------------
# add - keyword arugument

add1 = lambda n1, n2: n1 + n2

# print(add1(n2=3, n1=2))
# -------------------------------------
# add - defaut arugument

add1 = lambda n1=2, n2=3: n1 + n2

# print(add1())

# -------------------------------------
# add - arbitary positional arugument

add1 = lambda *args: args

# print(add1(1, 2, 3, 4, 5, 6, 6, 7, 7))  # it return it in tuple

# -------------------------------------
# add - arbitary keyword arugument

add1 = lambda **kwargs: kwargs

# print(add1(p=1, w=3, i=4, d=8, s=8, m=12))  # it return it in dictionary

# ---------------------------------------

# higher order function -
# explain - a function which take another function as a argument or return a function as result called as higher order function

# -----------------------------------------
# ex - of higher order function - the f2 is the higher order function here


def f1():
    pass


def f2(func):  # is the higher order funtion
    pass


# f2(f1)

# --------------------------------------------
# python has inbuild higher order functions -
# 1. filter

# numbers = [10, 20, 30, 40, 50, 60]

# def fun(num):
#     if num > 35:
#         return True
#     else:
#         return False


# fil = filter(fun, numbers)
# fil = list(filter(fun, numbers))
# print(fil)

# --------------------------------------------
# filter even number only

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


filtered = filter(is_even, numbers)  # filter function return filter object


# print(list(filtered))  # [2, 4, 6, 8]

# --------------------------------------------
# by using lambda function -

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

filtered = filter(
    lambda num: num % 2 != 0, numbers
)  # filter function return filter object


# print(list(filtered))  # [2, 4, 6, 8]

# ------------------------------------------
# filter starts with a

student = ["pavan", "ajay", "arun", "vijay", "rahul", "amar", "sujay", "atul"]

starts_with = filter(lambda student: student[0] == "a", student)

# print(list(starts_with))

# --------------------------------------------
# filter ends with y

student = ["pavan", "ajay", "arun", "vijay", "rahul", "amar", "sujay", "atul"]

ends_with = filter(lambda student: student.endswith("jay"), student)

# print(list(ends_with))

# ----------------------------------------------
# wap to print list of names of pass student

student = {
    "pavan": 89,
    "ajay": 45,
    "arun": 21,
    "vijay": 90,
    "rahul": 10,
    "amar": 77,
    "sujay": 23,
    "atul": 81,
}

pass_students = list(filter(lambda student: student[1] > 40, student.items()))
print([student[0] for student in pass_students])

#-------------------------------------------------
#



#-------------------------------------------------

# timeframe 1:23:00
