# return statement -

# ------------------------------

# scope -
# globle scope or space -
# explain - entire "space outside of the function" called as globle scope
# and the variable which is defined in globle scope called as globle scope variable
# we can access globle variable inside a function

# local scope or space -
# explain -  a "space within the function" called as local scope
# and the variable which is defined in local scope called as local scope variable
# you can access local variable within a function
# we can access globle variable both inside function and outside function
# we can access globle variable but can't change in it , for that use global keyword
# we can use local variable within a function but can't access it outside the  function

# globle keyword -
# explain -  The global keyword in Python is used to indicate that a variable inside a function (or another local scope) refers to the variable in the global scope (module level), rather than creating a new local variable
# if you want to update the value of globle variable from local scope (function) the you can use globle keyword so it will affect the globle variable only when the variable name is same in both local and globle scope

# return statement -
# explain - return is a predefined keywords in python, it is used to send value back to the function caller
# the code after return statement will not be execute when the function is called
# if you pass on value in return it will return one object but if you pass multiple value in return it will return in tuple (data type)
# it will return the value to the function caller

# ------------------------------

# for ex -
# outside function was globle scope
x = 19
y = 20


def f1():  # inside function was local scope
    a = 100
    b = 200
    print(a, b)  # 100 200
    print(x, y)  # 19 20


# f1()

# ------------------------------

x = 10
y = 20


def f1():
    a = 100
    b = 200
    # x = 300  # this is a new local variable
    global x  # this will tell python to use globle variable x instead of creating new local variable
    x = 300
    print(
        x, y
    )  # 300 20 - and 300 because new local variable is created with same name as locale variable


# --------------------------------

# Today topic -

x = 10  # globle variable
y = 20  # globle variable


def f1():
    a = 199  # local variable
    print(a)
    print(x)
    y = 299  # local variable - python will create new local variable , so the globle variable y will not be affected
    print(y)


# f1()

# print(
#     y
# )  # 20 - because the globle variable y is not affected by the local variable y so it's value remain the same

# --------------------------------
# if you want to update the value of globle variable from local scope (function) - use globle keyword  -

x = 10  # globle variable
y = 20  # globle variable


def f1():
    a = 199  # local variable
    print(a)
    print(x)
    global y
    y = 299  # after usign global keyword - now this will update the globle variable y (it will not create new local variable y anymore)
    print(y)


# f1()

# print(
# y
# )  # 299 - because the globle variable y is not affected by the local variable y so it's value remain the same


# ----------------------------------

count = 0  # global variable


def register(name, course):
    print(f"name: {name} course: {course}")
    global count  # after this i can update the global count from local scope
    count = count + 1


# register("Adinath", "blockchain developer")
# register("rushank", "ml developer")
# register("kirtan", "web3 developer")

# print(count)

# -----------------------------------
# if you want to use local scope variable outside the function


# def add(n1, n2):
#     result = n1 + n2
#     print(result)


# add(10, 20)
# print(result**2) # this will throw an error , because result is a local variable

# --------------------------------------
# return statement - return is a predefined keywords in python, it is used to send value back to the function caller


def percentage(part, total):
    res = (part / total) * 100
    # print(res)
    return res


# percentage(280, 500)
# print(percentage(280, 500))  # 56.0

# if percentage(280, 500) > 50:
#     print("pass")
# else:
#     print("fail")


# ----------------------------------------
# code after return statement will not be executed
# def square(num):
#     sq = num**2
#     print("welcome")
#     return sq
#     print(
#         "hello"
#     )  # after return the next line will not be executed it the function will terminate


# print(square(4))
# print("coding.....")

# -------------------------------------------
# if you want to return multiple value from the function


# def add(n1, n2):
#     return n1, n2, n1 + n2


# print(add(10, 20))  # (10, 20, 30)

# -------------------------------------------
# how to return multiple value from the function in python
# if you pass multiple return value then it will return it  in tuple (data type)


def calci(n1, n2):
    add = n1 + n2
    sub = n1 - n2
    mul = n1 * n2
    return add, sub, mul


# print(calci(10, 20))
# x = calci(4, 7)
# add, sum, mul = calci(10, 5)

# print(add)
# print(sum)
# print(mul)


