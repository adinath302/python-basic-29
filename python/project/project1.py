# project - 1

# collective data types -

# list [1,2,f] - mutable
# set {d,5} - mutable
# dict {1,3,3} - mutable
# fsrozenset { 1,2} - immutable
# tuple ()  - immutable
# string "hello" - immutable

# ------------------------

# i = [11,22,33,44,55,66,77]

# for s in i:
#     print(s);

# ------------------------

# syntax of while loop - ICU

# initialization -1
# while condition: -2
#     code
#     update -3

# while condition: # till the condition is true the code will be executed.
#     code

# -------------------------

# i = [11, 22, 33, 44, 55, 66, 77]

# index = 0  # initialization

# while index < len(i):  # condition
#     print(i[index])  # code (print through indexing)
#     index = index + 1  # update
# output --
# 11
# 22
# 33
# 44
# 55
# 66
# 77

# -------------------------

# calculator using while loop

# con = "yes"  # initialization
# while con != "no":  # condition
#     n1 = eval(input("Num1: "))
#     opr = input("Operator: ")
#     n2 = eval(input("Num2: "))
#     if opr == "+":
#         print(n1 + n2)
#     elif opr == "-":
#         print(n1 - n2)
#     elif opr == "*":
#         print(n1 * n2)
#     elif opr == "/":
#         print(n1 / n2)
#     else:
#         print("Invalid operator")
#     con = input("Do You want to continue (yes/no): ")  # update

# --------------------------

# wap to check no is perfect or not


# num = int(input("enter a number: "))
# sum = 0
# for i in range(1, num):
#     if num % i == 0: # check if the i is divisor of num
#         sum = sum + i # sum of number which are divisor of num
# if sum == num:
#     print(num, "is a perfect number")
# else:
#     print(num, "is not a perfect number")

# --------------------------

# numbers = [1, 2, 3, 4, 5]
# sum = 0
# for num in numbers:
#     sum = sum + num
# print("Sum:", sum)

# --------------------------

# multiply all the numbers
# numbers = [1, 2, 3, 4, 5]
# sum = 1
# for num in numbers:
# sum = sum * num

# --------------------------

# wap to cal sum of num from 1 to 50

# sum = 0 # initialization of sum
# for a in range(1, 51): # loop from 1 to 50(start,end,step_value(default is 1))
#     sum = sum + a # sum update
# print("Sum:", sum)

# --------------------------
# perfect or not number - this code is written by using sequencial programming

# num = int(input("enter a number - "))
# sum = 0  # sum of i (which are divisible by num)
# for i in range(1, num): # iterate the numbers from 1 to num to apply logic in it
#     if num % i == 0: # if the reminder is 0
#         sum = sum + i
# if sum == num:
#     print(f"{num} is a perfect number")
# else:
#     print(f"{num} is not a perfect number")

# ----------------------------

# wap to say number is Armstrong or not .

# num = str(input("enter a num - "))  # take input as string
# sum = 0  # initialization of sum
# for i in num:  # iterate through each digit in num "123" = '1','2','3' - still string
#     sum = sum + int(i) ** len(num) # int(i) - convert string digit to integer(1,2,3)
# if sum == int(num):
#     print(f"{num} is a Armstrong number")
# else:
#     print(f"{num} is NOT Armstrong number")

# ----------------------------

# Armstrong number or not  -

# num = str(input("enter a num -"))  # str because it's iterable
# sum = 0
# for i in num:
#     sum = sum + int(i) ** len(num)
# if sum == int(num):
#     print(f"{num} is a Armstrong number")
# else:
#     print(f"{num} is NOT a Armstrong number")

# ------------------------------

#  wap to say number is prime number or not 


# timeframe  - 1:45:43