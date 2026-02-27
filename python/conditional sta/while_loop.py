# while loop - 👇
 

# looping statement 👇-

#  1. for loop - 👇 - used as a looping statement , only when you know how many times you want to loop
#  2. while loop -  👇 -
# # initializatoin condition update  - while loop syntax


# iterable - list, tuple , string, dict, set, range

# i = [1, 2, 3, 4, 5]  # this is an iterable
# for s in i:
#     print(s)  # this is how we use for loop

# student = []
# for i in range(10):
#     name: input("enter your name")
#     student.append(name)

# print(student)

# stu_data = {}
# ex
# for s in range(5):  # range will loop the for loop 5 times
#     name = str(input("enter your name - "))
#     data = int(input("enter your data - "))
#     stu_data[name] = data

# print(stu_data)

# till now we know exactly how many times we want to loop but when we don't know how many times we want to loop we use 'while loop'

# while loop - looping statement

# while condition: # while the condition is true the code will be executed.
# body
# code

# ex
# while True:
#     print("hello")

# while False:
#     print("hello")

# initializatoin condition update  - while loop syntax
# num = 10  # initialization
# while num < 15:  # it will re-run until the "condition" is false
#     print("hello")
#     num = num + 1  # - update

# when to use
# when i know about number of iterations use - for loop
# and when i don't know about number of iterations use - while loop

# ex 1 .- while loop syntax - initialization - condition - update
# student = [] # to store the values
# cont = "yes"  # initialization

# while cont == "yes":  # condition( while the cont is true the code will will execute )
#     name = input("enter your name - ")  # code
#     student.append(name)
#     cont = input("do you want to continue - (yes/no)")  # update
# print(student)

# ex 2.

# stu = {}
# ss = "yes" # condition initialization

# while ss == "yes": # actual condition
#     name = str(input("enter name - "))
#     data = int(input("enter data - "))
#     stu[name] = data # till this line - code
#     ss = str(input("enter yes/no - ")) # update
# print(stu)

# # ex
# user_name = "ketan"
# password = "ki123"

# name = ""
# passw = ""

# while (
#     name != user_name or passw != password
# ):  # until the name is not equal to user name and password is not equal to password it will run the code
#     name = str(input("enter name - "))
#     passw = str(input("enter password - "))
# print("login")

# ex signup -
# username could be anything but t
# but the password should contains more than 6 charactor to create account
# until it not give more than 6 ch print please enter password again

# stu = {}
# username = ""
# password = ""
# username = str(input("enter your name - "))

# while len(password) < 6:  # it will run until it's true
#     password = eval(input("enter the password - "))

# stu[username] = password
# print("sign up")


# transfer statement - 👇 - 3 types of statements

# 1. pass - 
# 2. break
# 3. continue

# pass 👇 - pass is a null operation statement; nothing happens when it executes. It acts as a placeholder where syntax requires a statement but where you, the programmer, don't want any code to run

# timeframe - 1:33:57


# end