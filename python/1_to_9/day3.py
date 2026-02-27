# -- day 3 of python
# -- parameter

# /n  --- for new line
# example
# print("hello \nworld")

# /t  --- for tab -- by defult spacing value is 4
# example by defult spacing value is 4
# print("hello \t world")

# print("\tAdinath gaware \n\tsoftware developer,trader \n\tand entrepreneur")

# -- parameter --

# n1 = 100
# n2 = 200
# n3 = 300
# print(n1, n2, n3,) # sep is a attribute

# name = "kunal"
# course = "blockchain developer"
# fees = 499

# print(name, course, fees ,sep="-",end="&")

# print(name, end="" , sep=" ") # end is a attribute by defult it is \n
# print(course, end="")
# print(fees, end="")

# num1 = 10
# num2 = 20
# sum = num1 + num2
# # print(sum)  # 30
# # print("sum of", num1, "and", num2, "is", sum) --
# print(
#     "sum of %d and %d is %d" % (num1, num2, sum)
# )  # %d is a format specifier for integer

# name = "kunal"
# mid = "rishabh"
# lst = "shinde"
# print(
#     "my name is %s %s %s" % (name, mid, lst)
# ) # %s is a format specifier for string or character

# example
n1 = 15.43
n2 = 2.34
sum = n1 + n2
# print("sum of %f and %f is %f" % (n1, n2, sum))  # %f is a format specifier for float 
print("sum of %0.3f and %0.3f is %0.3f" % (n1, n2, sum))   # %f is a format specifier for float and the "o.3f" is to limit the numbers after decimal(.) you want


# example
# no = 9
# square = no * no
# print("the square of %d is %d" % (no, square))
