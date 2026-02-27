# type of arguments -

# function
# > parameter
# > argument
# >> types

# ------------------------------
# revision -
# function
# definition and calling
# parameter - parameter are the variable which is defined inside a parenthisis at a time of function defination

# ------------------------------
# wap to calculate mean of 4 numbers


def mean(a, b, c, d):
    res = a + b + c + d
    ta = res / 4
    print(ta)


# mean(2,3,4,5)

# ------------------------------
# area of reactangle -


def a_reactange(l, w):
    A = l * w
    print(A)


# a_reactange(10,12)

# -----------------------------
# Todays topic
# argument type-
# 1. positional argument
# 2. keyword argument (parameter with default value)
# 3. default argument
# 4. arbitary arguments
# if we mix both then we have to use positional argument first then keyword argument second , if not it will show error
# in the case of default argument also fist we use without default arguments then with default argument


# positional argument - as per position of argument , no of parameter and argument should be same
# example
def fullname(fn, mn, In):
    fname = f"{fn} {mn} {In}"
    print(fname)


# fullname('vijay','ramdas', 'kale')
##vijay ramdas kale
# fullname('ramdas', 'vijay','kale')
# ramdas vijay kale

# ------------------------------
# keyword argument - no need to maintain position as per function defination , but no of parameter and argument should be same
# example


def fullname(fn, mn, In):
    fname = f"{fn} {mn} {In}"
    print(fname)


# fullname(fn="vijay", mn="ramdas", In="kale")

# ------------------------------
# mix positional and keyword argument - if we mix both then we have to use positional argument first then keyword argument second


def fullname(fn, mn, In):
    fname = f"{fn} {mn} {In}"
    print(fname)


# fullname("vijay", mn="ramdas", In="kale")


# ------------------------------
# default argument - parameter with default value if we don't pass argument it will take default value
def fullname(fn, mn="ramdas", In="kale"):
    fname = f"{fn} {mn} {In}"
    print(fname)


# fullname("vijay")


# ------------------------------
# cf charecter is available in the string or not -
def find_char(my_string, char_to_find):
    if my_string.find(char_to_find) != -1:
        print("yes")
    else:
        print("no")


# find_char("hello world", "o")

# ------------------------------------


def search(word, char):
    for i in word:
        if i == char:
            print("yes")
            break
    else:  # the else is for for loop
        print("no")


# search("vaibhav", "p")

# --------------------------------
# arbitary arguments :
# explain - when we don't know how much arguments i have to take
# types of arbitary arguments
"""
positional arbitary arguments - it will collect the data in *args as a tuple(data type)
keyword arbitary arguments - 
"""

# ----------------------------------
# ex - this is a normal function where we can't pass more arguments than defined parameters , both should be same
def add(n1, n2):
    print(n1 + n2)


add(
    1, 2
)  # here i know exactly how much argument i need to give , but when i don't know about that then we use arbitary argumet


# -----------------------------------
# ex - positional arbitary arguments with *args
# explain - we use *args when we are passing multiple positional arguments , when we don't know how much argument should be passed and it will stored in the form of tuple
def add(*args):
    sum = 0
    # print(args)  # (10, 20)
    # pass # we use it when i don't know what to write inside a function , and we don't want error
    for i in args:
        sum = sum + i
    print(sum)


# add(10, 20, 40, 23) # you can pass multiple arguments

# -----------------------------------
# ex -


def details(name, age, course):
    data = f"""
    name: {name}
    age: {age}
    course: {course}
     """
    print(data)


# details("vaibhav", 24, "python") # this is positional argument(normal)
# details(name="vaibhav", course="python", age=24)  # this is keyword argument


# -----------------------------------
# ex - this is keyword arbitary arguments with **kwargs
# explain - we use **kwargs when we are passing keyword arbitary arguments, when we don't know how much keyword argument should be passed and it will stored in the form of dictionary
def details(**kwargs):
    print(kwargs)  # {'name': 'vaibhav', 'age': 24, 'course': 'python'}


details(name="vaibhav", age=24, course="python", city="pune")

# if you want to accept multiple keyword arguments then you have to use **kwargs
# explain - what ever the keyword argument we pass it will collect in the form of 'dictionary'

# -----------------------------------


