# methods in python

# both methods and functions are reusable block of code ⤵
# 1. method
# 2. function

# explain method - method is a function which is defined inside a class
# explain function - function is a reusable block of code which is used to perform some operation on data


# for example -
def square():  # def is a keyword to define a function(reusable)
    num = int(input("num: "))
    square = num**2
    # print(square)


# square()  # this is a function call & you can call it from everywhere in your program after importing the function

a = 123
# all data types in python is considered as a object , all the operations related to that data type are stored inside of that class of that data type and you can use it directly

# string methods - ⤵

# 1. upper()
name = "hello world"  # this is a string object
name.upper()  # method - object refrence and method name and "()"
# print(name.upper())

# 2. lower()
lname = "HELLO WORLD"
lname.lower()
# print(lname.lower())

# 3. title() -string method used to convert a string to title case where each word starts with a capital letter
dname = "hello world"
dname.title()
# print(dname.title())

# 4. capitalize() -the first word starts with a capital letter
cname = "hello world"
cname.capitalize()
# print(cname.capitalize())

# 5. swapcase() - Swaps the case of all characters (uppercase becomes lowercase and vice versa). "HeLlO".swapcase() returns 'hElLo'
sname = "Hello World"
sname.swapcase()
# print(sname.swapcase())

# 6. casefold() - Similar to lower(), but more aggressive for case-insensitive comparisons across various Unicode characters (e.g., converts the German 'ß' to 'ss').
nname = "Hello World"  # this is an object , python will allocate memory to it and store the value and the variable name is like a refrence name for it
c = (
    nname.casefold()
)  # but after this the memory location will changed with the refrence name (c) to check the memory location we use id()
# print(c)

# 7. isalpha() - Returns True if all characters in the string are alphabetic
wname = "HelloWorld"
wnames = "Hello World"
wnamess = "HelloWorld223"
wname.isalpha()
# print(wname.isalpha())
# print(wnames.isalpha())
# print(wnamess.isalpha())

# 8. isnumeric()
su = 233  # this object is of integer , and the isnumeric method/operation was of string it will show error
sui = "343"  # true
suiq = "3.43"  # false
suii = "sdf"  # false
sui.isnumeric()
# print(suiq.isnumeric())
# print(sui.isnumeric())
# print(suii.isnumeric())

# 9. isupper
# 10. islower
# 11. istitle

# 12. replace() # replace the old sub-string with the new sub-string
cls = "hello world"
cls.replace("hello", "hi")
# print(cls.replace("hello", "hi"))

# 13. index # a built-in function used with sequence data types (such as lists, strings, and tuples) to find the position of the first occurrence of a specified element. it takes the element as an argument and in optinal index from which the search should start and The index at which the search should end returns the index of the first occurrence of the element
llo = "hello world"
llo.index("world")
# print(llo.index("o")) # 4
# print(llo.index("r")) # 8
# print(llo.index("o",5)) # 7 - to get the index of secound "o"

cls = "i am the king of this world"
# print(cls.index("k"))
# print(cls.index("i", 11))
# print(cls.index("s"))

# task 1

x = "python is a programming language , python is a simple , python is dynamic"
x.replace("python", "Python")
# print(x.replace("python", "PYTHON"))

# task 2
x = "python is a programming language, python is a simple, python is dynamic"
print(
    x.replace("python", "PYTHON", 2)
)  # "2"-parameter will replace the first 2 python with PYTHON

# task 3 - to get the number of a character
x = "python is a programming language, python is a simple, python is dynamic"
print(x.count("p"))
print(x.count("p", 5))
print(x.count("p", 5,18))


# print(id(nname)) # this will give you the memory location "1984628958192"
# print(id(c)) # this will give you the memory location "1984628956784"

# -- string is a collection of character is immutable and ordered data type , but if you change the string it will return a new string with new memory location of it .

# -- if you use the used string variable name for another string then python garbage collector will dealocate the previous value and allocate the new value to the memory location of the same refrence name

a = "hhh"
a = "FFF"
# -- it will print the last value "FFF"
# print(id(a))


# -- operations/methods related to an object is stored inside of it's class like this string related operations/methods are stored inside of string class and "you can use string methods only on string object" and not on other data types.

# example

per = 87  # this is a integer object
per2 = "23"  # this is a string object

# c = per.isnumeric # it will show error 'int' object has no attribute/method 'isnumeric'
# print(c)
# d = per2.isnumeric()  # it will show "true"
# print(d)

# done