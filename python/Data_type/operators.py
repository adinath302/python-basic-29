# todays topic -

# operators in python - are used to perform mathmetical operations on data
# >- arithmetic operators
# >- assignment operators
# >- comparison operators
# >- logical operators
# >- identity operators
# >- membership operators

# Revision  -
# iteration
# for loop
# test

# what is data type in python -
# - A data type in Python is a classification that specifies the kind of value a variable can hold and determines the operations that can be performed on it

# for loop syntax -
# iterable means collection of data or object which can be iterated

# for variable name in iterable/range:
# body

# -------

# arithmetical operators in pythons :👇
# explain - operators are a special symbols in python that are used to perform some operation on data

# chatgpt prompt for practice python - for example
# for loop in python ask me tricky questions at expert level
# do not ask me programming questions
# real time examples of for loop in

# ------ operators ------
# 1. +  plus -
# if 1 + 3 = 4 this is called addition
# if 9 + 6 = 9 this is called addition
# but if "tara" + 'singh' = 'tara singh' this is called concatenation
# if [1,2,3] + [4,5,6] = [1,2,3,4,5,6] this is called list concatenation
# if ('ketan','rahul') + ('rupali'+'ganesh') = ('ketan','rahul','rupali'+'ganesh') this is called tuple concatenation
# it does not support "set" and "dictionary" concatenation

# 2. -   minus subtraction
# subtraction operator only support int and float

# 3. *  multiply
# you can multiple int with int
# you can multiple int and float
# you can multiple string with integer(it will repeat the string as many times as the integer's value is given)
# you can multiple list with integer(it will repeat the list as many times as the integer's value is given)
# you can multiple tuple with integer(it will repeat the tuple as many times as the integer's value is given)
# it does not support for set and dictionary


# / - division operator
# allways return float value (quotient value)
# print(10/4) # 2.5
# print(-10/3) # -3.3333333333333335
 
# // - floor division operator
# allways return int value (small value)
# print(10//3) # 3
# print(-10//3) # -4

# **  power operator
# used when you want to raise one number to the power of another number
# print(5**2)

# %   modulus operator
# it will return the remainder
# print(10 % 5)

# comparison/relational operator in python - 👇
# explain - it is used to compair two or more values and return a boolean value (True or False)

# 1. ==  equal to
# 2. !=  not equal to
# 3. >   greater than
# 4. <   less than
# 5. >=  greater than or equal to
# 6. <=  less than or equal to

# examples -

n1 = 100
n2 = 12
print(n1 > n2) # True
print(n1 < n2) # false
print(n1 == n2) # false
print(n1 <= n2) # false
print(n1 >= n2) # true
print(n1 != n2) # true


# --------------------------

# every value inside a variable has a data type and every data type has class , every class has predefined methods of that data type

#
# "data type" will tell you which type of value is stored inside a variable, and what operations can be performed on that data

# dir() - function return all the methods of that data type / attributes
# --- this function will tell you what are the operation can be performed on that data type
