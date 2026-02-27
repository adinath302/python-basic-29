# map and reduce in python

# ---------------------------------

# normal function
# def fname(parameter):
# body
# operation
# return result

# --------------------------------------------
# lambda function -

rev = lambda word: (word[::-1], word.upper())
# print(rev("pranav"))

result = lambda per: "pass" if per >= 40 else "Fail"
# print(result(30))  # true

# ----------------------------------------------
# eligible for voting -

vote = lambda age: "eligible for voting" if age > 18 else "Not eligible for voting"
# print(vote(16))

# ------------------------------------------------
# filter even numbers
x = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100, 16]
o = tuple(filter(lambda num: num % 2 == 0, x))  # it takes a function and a iterable
# print(o)

# --------------------------------------------------
# wap to salary etween 20k to 40k filter data
emp_salary = {
    "kunal": 67000,
    "kiran": 77000,
    "karan": 21000,
    "vijay": 34000,
    "arun": 24000,
    "sujay": 89000,
}
# filter(fun, iterable)
# lambda parameter : expression (logical statement)
is_salary = dict(
    filter(lambda item: item[1] > 20000 and item[1] < 40000, emp_salary.items())
)

# print(is_salary)

# -----------------------------------------------------
# map function -
# map(function, iterable) -
# map is a higher order function in python it takes a function and an iterable as a argument and returns a map object, this function is applyed on every element of the iterable and returns a map object.
# map return an object you have to convert it into a list or tuple or set or any other iterable type
# -----------------------------------------------------
# for ex -1 - how map function works
numbers = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]

# print(map(lambda num: num / 2, numbers))

# ------------------------------------------------------
# ex no 2 -

student = {
    "pavan",
    "ajay",
    "arun",
    "vijay",
    "rahul",
    "amar",
    "sujay",
    "atul",
}

is_titile = map(lambda stu: stu.title(), student)


# print(is_titile) - <map object at 0x00000194E25BB8C0>

# print(
# list(is_titile)
# )  # -['Rahul', 'Sujay', 'Pavan', 'Arun', 'Amar', 'Atul', 'Vijay', 'Ajay']
0
# because the map function is return object you have to convert it into a list or any other data type

# -----------------------------------------------
# dict of square of each number -

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

is_square = dict(
    map(lambda num: (num, num**2), numbers)
)  # (num, num**2) it's key and value pair

# print(is_square)

# -----------------------------------------------
# salary increased by 2000 and return a dict -

emp_salary = {
    "kunal": 67000,
    "kiran": 77000,
    "karan": 21000,
    "vijay": 34000,
    "arun": 24000,
    "sujay": 89000,
}

is_insalary = dict(map(lambda item: (item[0], item[1] + 2000), emp_salary.items()))

print(is_insalary)

# ------------------------------------------------
# reduce function -

numbers = [10, 20, 30, 40, 50]

from functools import reduce

print(reduce(lambda sum, num: sum + num, numbers))


# timeframe -  1:13:00
