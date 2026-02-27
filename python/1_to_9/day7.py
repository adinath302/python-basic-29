# Day 7 of python

# topic to cover -- 4
# input function
# type casting
# eval
# programs

# name = "Adinath"
# print("hello", name)

# -- input function -- 👇 1
# it is used to get the input/value from the user

# for example

# name = input("Enter your name")

# print("hello", name)

# example no 2

# course = input("Course Name - ")
# duration = input("Duration - ")
# trainer_name = input("traner name - ")

# print("Course name", course)
# print("Duration", duration)
# print("Trainer name", trainer_name)

#  wap to cal square of any number from the user.

# num = input("Enter a number - ")
# print(type(num))
# square = int(num) * int(num) # converting any data type to another is called as type casting
# print(f"the square of {num} is {square}")

# input function only return string value
# x = input("enter something:")
# print(type(x))
# print(x)

# type casting -- 👇
# explain - converting a data type to another data type
# example 1  -

# num = 189.99  # data type float
# print(type(num))
# num = int(num)  # converted the data type from float to int
# print(type(num))

# example 2

# marks = 89
# print(type(marks)) # to check the data type
# marks = float(marks) # converted a int to float
# print(marks)
# print(type(marks))

# example 3

# x = int(input("enter a number - "))  # another way of type casting(string to int)
# print(type(x))
# print(x)

# x = float(
#     input("enter a number - ")
# )  # another way of type casting(string int to float)
# print(type(x))
# print(x)

# x = list( # list is a versatile, built-in data structure that stores an ordered collection of items
#     input("enter a number - ")
# )  # another way of type casting(string int to list)
# print(type(x))
# print(x)

# num = "1345"
# print(type(num))
# num = int(num)
# print(type(num))
# print(num)

# num = "ten" # this will never work because only numric string can be converted to int(number)
# num = int(num)
# print(type(num))
# print(num)

# percentage = "89.78"
# percentage = float(percentage)
# print(type(percentage))
# print(percentage)

# percentage = float(input("enter your percentage -"))
# print(type(percentage))
# print(percentage)

# eval function -- 👇
# explain - dynamically evaluate and execute a string as a Python expression and returns the result

# example 1 -

# x = eval(
#     input("enter a expression - ")
# )  # eval function is used to evaluate the expression, if the input is "asdfds" it will show string value, if the input is 12 it will show int value, if the input is 12.67 it will show float value
# print(type(x))

# example 2 -

# y = eval(input("enter anything -"))
# print(type(y))
# print(y)
# print(type(y))

# example 3 -

# y = input("enter a mathematical expression - ") # input function always return string value(data type)
# print(type(y)) # to check the data type
# x = eval(input("enter a mathematical expression - "))
# print(type(x))
