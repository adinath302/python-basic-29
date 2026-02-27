# exception handling -
# python exceptions -

# --------------------------------------------------------------
# num1 = eval(input("num1: "))
# num2 = eval(input("num2: "))

# try:
#     div = num1 / num2
# except:
#     print("we cant divide by zero")

# print(div)  # 10 / 0 - zero division error called as exception error

# --------------------------------------------------------------
# why we use exception handling -


def count(file):
    f = open(file, "r")
    lines = f.readlines()
    c = len(lines)
    return c


# print(count('File & Exception Handling/d1.txt'))
# print(count('File & Exception Handling/d2.txt'))

# --------------------------------------------------------------
# words calculate -

result = {"kunal": 56, "umesh": 89, "rakesh": 78, "sharma": 90, "vishal": 90}


def marks(name, dict):
    mr = dict[name]
    return mr


# print(marks("suraj", result))  # after this exception will occur


# --------------------------------------------------------------
# how to handle exception -

"""

try:
    risky code                  # chances of exception/error

except:
    code to handle exception

else:
    code to execute if there is no exception

finally:
    code to execute always

"""


# --------------------------------------------------------------
# ex

# num1 = eval(input("num1: "))
# num2 = eval(input("num2: "))

# sum = num1 + num2
# sub = num1 - num2
# mul = num1 * num2
# div = num1 / num2

# try:
#     div = num1 / num2
# except:
#     print("we cant divide by 0")
# else:
#     print(f"div of {num1} and {num2} is {div}")
# finally:
#     print(f"sum of {num1} and {num2} is {sum}")
#     print(f"sub of {num1} and {num2} is {sub}")
#     print(f"mul of {num1} and {num2} is {mul}")

# --------------------------------------------------------------
# ex - name error

# try:
#     num1 = eval(input("num1: "))
#     num2 = eval(input("num2: "))
#     div = num1 / num2
# except ZeroDivisionError:
#     print("we cant divide by 0")
# except NameError as e:
#     print(e)
# else:
#     print(div)
# print("coding....")

# --------------------------------------------------------------
# raise -
# value error

# age = int(input("enter age : "))
# if age < 0:
#     raise ValueError("age can't be negative")
# if age>100:
#     raise ValueError('age can not be greater than 100')
# print(f"my age is {age}")


# --------------------------------------------------------------
# custom exception creation -
# ex -
# class fiveDivisionError(Exception):
#     pass


# n1 = 10
# n2 = 5
# if n2 == 5:
#     raise fiveDivisionError("division by 5")  # object with argument
# print(n1 / n2)


# --------------------------------------------------------------
# custom exception class in details
# class LimitEndError(Exception):
#     def __init__(self, msg):
#         self.msg = msg

#     def __str__(self):
#         return self.msg


# amount = eval(input("enter amount"))
# if amount > 20000:
#     raise LimitEndError("limit end")
# print("done")

# --------------------------------------------------------------
# indexing error

# l = [11, 22, 33, 44]
# print(l[4])
# # --------------------------------------------------------------
# caf to count no of characters in given files
# def count():
#     f = open('File & Exception Handling/demo1.txt','r')


# --------------------------------------------------------------


def count_lines(file):
    try:
        f = open(file, "r")
    except FileNotFoundError:
        file = input("enter corrrect file name : ")
        count = count_lines(file)
        return count
    else:
        lines = f.readlines()
        c = len(lines)
        return c

print(count_lines("File & Exception Handling/d2.txt"))

# --------------------------------------------------------------

# module - reusable variable function class

'''




'''


# --------------------------------------------------------------
# shalow copy - copy only one level(outer level)
#  and deep copy - copy all levels

numbers = [[10,20],[30,40],[50,60]]
new_numbers = numbers
print(new_numbers)
print(id(numbers))
print(id(new_numbers))

# copy - 


# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------
