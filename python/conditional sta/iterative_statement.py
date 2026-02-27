# iterative statement - 👇
# while loop - 👇

# revision -

# if
# elif
# else

# ex
# marks = int(input('marks : '))

# if marks >=90:
#     print('A+')
# elif marks >= 80:
#     print('A')
# elif marks >=70:
#     print('B+')
# elif marks >=60:
#     print('B')
# else:
#     print('c')

# print('coding...')


# ex - calculator -

# f1 = eval(input("enter first amount - "))
# f2 = eval(input("enter second amount - "))
# operator = str(input("what you want to do with them - "))

# result = ""
# if f1 >= 0 and f2 >= 0:
#     if operator == "+":
#         result = f1 + f2
#     elif operator == "-":
#         result = f1 - f2
#     elif operator == "*":
#         result = f1 * f2
#     elif operator == "/":
#         result = f1 / f2
#     else:
#         print("invalid operator")
# else:
#     print("one of then is negative number")


# print(f"{f1} {operator} {f2} = {result}")


# ex 2 - user - bill amount
# apply discount  if bill amount  2k - 4k dis 5% , 4k - 6k dis 10% , 6k - 10k dis 15% , > 20k dis 20%
# dis_amount = ""

# bill = int(input("enter amount - "))

# if bill >= 2000 and bill < 4000:
#     discount = 5 / 100 * bill
#     dis_amount = bill - discount
# elif bill >= 4000 and bill < 6000:
#     discount = 5 / 100 * bill
#     dis_amount = bill - discount
# elif bill >= 6000 and bill < 10000:
#     discount = 15 / 100 * bill
#     dis_amount = bill - discount
# elif bill >= 10000:
#     discount = 20 / 100 * bill
#     dis_amount = bill - discount
# else:
#     dis_amount = bill
# print(f"discounted price - {dis_amount}")


# ex - number is divisible by 3
# or divisible 5
# or divisible by 3 and 5
# and number is not divisible by 3 and 5

# num = int(input("enter a number- "))

# if num % 3 == 0 and num % 5 == 0:
#     print(f"{num} is divisible by 3 and 5")
# elif num % 3 == 0:
#     print(f"{num} is divisible by 3")
# elif num % 5 == 0:
#     print(f"{num} is divisible by 5")
# else :
#     print(f"{num} is not divisible by 3 and 5")


# ex -
# unit - price per unit
# 0-100 =  5
# 100 - 500 = 10
# 500 -  700 =  15
# > 700 = 20 per unit

# bill = ""

# unit = int(input("enter total unit - "))
# if unit >= 0 and unit < 100:
#     bill = unit * 5
# elif unit >= 100 and unit < 500:
#     bill = unit * 10
# elif unit >= 500 and unit < 700:
#     bill = unit * 15
# else:
#     bill = unit * 20
# print(bill)


# student_marks = {
#     "raj": 67,
#     "amar": 89,
#     "vijay": 89,
#     "vishal": 91,
#     "vaibhav": 97,
#     "nayan": 21,
#     "bhushan": 66,
#     "varun": 77,
#     "atul": 88,
#     "vinod": 34,
#     "bhakti": 55,
# }
# # print dict -key =name , value = grade

# stu_grade = {}

# for name, marks in student_marks.items():
#     if marks >= 90:
#         stu_grade[name] = "A+"
#     elif marks >= 80:
#         stu_grade[name] = "A"
#     elif marks >= 70:
#         stu_grade[name] = "b+"
#     elif marks >= 60:
#         stu_grade[name] = "b"
#     else:
#         stu_grade[name] = "c"

# print(stu_grade)
# timeframe - 1:13:00