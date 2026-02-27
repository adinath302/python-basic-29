# flow control statement are use to control the execution flow of the program by using
# 1. conditional statement - 👇
# 2. iterative | looping statement - 👇
# 3. transfer statement - 👇

# ------------
# 1 - conditional statement - 👇
# ______________________________


# if condition:  # if the condition is true then only the block(code) will be executed
# this is if body
# code

# statement 1

# if cond:
# statement 2
# statement 4

# statement 5

# ____________________________----

# print("start")
# num = int(input("enter a while number"))
# if num > 5:
#     print(f"{num} is gt by 5")

# print("end")

# print("hello")

# num = int(input("enter a number "))
# if num % 6 == 0: # if it's true then only the block will be executed
#     print(f"{num} is divisible by  6")
# print("the end")

# wap to iterate number which is greater than 15;
# numbers = [11, 12, 14, 13, 15, 16, 17, 18, 19, 20]
# for num in numbers:
#     if num > 15:
#        print(num)

# wap to iterate even numbers only
numbers = [11, 12, 14, 13, 15, 16, 17, 18, 19, 20]
# for no in numbers:
#     if no % 2 == 0:
#         print(no)

# ex - odd numbers
# for no1 in numbers:
#     if no1 % 2 != 0:
#         print(no1)

# ex - wap a program to print number which are between 13 to 18
# for l in numbers:
#     if l >= 13 and l < 18:
#         print(l)

# ex - wap

student = ["mayur", "amar", "om", "pranav", "rajesh", "ajay", "pratik", "sujay"]

# for name in student:
#     if name.startswith("a"):
#         print(name)

# for name1 in student:
#     if name1.endswith("jay"):
#         print(name1)

# for name2 in student:
#     if name2[0] == "a":
#         print(name2)

for name3 in student:
    if name3[-1:-3:1] == "jay":
        print(name3)




# timeframe 1:45:00