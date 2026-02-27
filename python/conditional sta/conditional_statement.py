# conditional statement  -

# last session -
# operators -
# > Arithmetic
# > comparison

# today's topic -
# operators -
# > Assignment
# > logical
# > identity
# > membership

# Assignment operator - 👇
# it is used to assign value to the variable

# =  assign to
# +=  add and assign
# -=  subtract and assign
# *=  multiply and assign
# /=  divide and assign
# //=  floor division and assign
# %=  modulus and assign
# **=  power and assign

# example - 1
num = 78
salary = 20000
# salary = salary + 5000
salary += 5000  # add and asign (salary = salary + 5000)
# print(salary)  # 25000

# example - 2
price = 100
price -= 10  # subtract and assign (price = price - 10)
# print(price)

# example - 3
car = 23
car *= 2  # multiply and assign (car = car *3)
# print(car)

# example - 4
p = 45
p /= 2  # divide and assign
# print(p)

# example -  5
a = 10
b = 3
a //= b  # floor division
# print(a)

f = 9000
f -= f * 10 / 100
# print(f)  # discounted f(value)

num1 = 10
num %= 5
# print(num)

# logical operator 👇 -

# it is used to connect two or more conditions and return a boolean value (True or False)

# - 1. and operator
# - 2. or operator

# and operator -

# ex 1
# p1        &        p2        final_result

# True     and      False         False
# False    and      False         False
# False    and      False         False
# True     and      True          True


# ex 2
# it will true if both the conditions are true otherwise false
# print(True and False)  # false
# print(False and False)  # false
# print(True and True)  # true

# or operator -

# ex 1
# print(True or False)  # true
# print(False or True or False)  # true
# print(False or False)  # false
# print(True or True)  # true

# - 3. identity operator (is ,is not) 👇-

# is - it is used to compare the memory location or id of two variables and return a boolean value (True or False)
# is not - it will return true if both the variables are same otherwise false

# interview question

# what is the diffrence between 'is' and '==' operator ?

num1 = 100  # int type obj
num2 = 100  # int type obj

# print(num1 == num2)  # to check the value (100)
# print(num1 is num2)  # to check the memory location

# both variable have same memory location ,
# because when you assign same value to both immutable variable it will stored in the same memory location in python

# ex 2 -

name1 = [1, 2, 3, 4]
name2 = [1, 2, 3, 4]

# print(name1 == name2)  # true
# print(
# name1 is name2
# )  # false - because mutable objects have different memory location even if the value is same

# is not -

name1 = [1, 2, 3, 4]
name2 = [1, 2, 3, 4]

# print(name1 != name2)  # false
# print(
# name1 is not name2
# )  # true - because mutable(changable) objects have different memory location even if the value is same

# membership operator - 👇

#  1. in
#  2. not in

# 1. in
# it will return true if the value is present in the variable otherwise false .
# example -
s = [3, 234, 2, 342, 4, 23, 5, 67, 8, 9, 8]
print(3 in s)  # true - because 3 is present in the list(s)
 
# 2.
# not in
print(78 not in s) # true - because 78 is not present in the list(s)


# flow control statement - 👇
# it is used to control execution flow of program 
# if you want to control flow/execution of program then you have to use flow control statement

# --- flow control statement used to control the flow of program
# 1. conditional statement - 👇
# 2. iterative | looping statement - 👇
# 3. transfer statement - 👇

# timeframe - 48:00
