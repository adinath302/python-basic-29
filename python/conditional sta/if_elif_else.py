# todays topic - if elif else
# if you have multiple conditions but you want to only one to run

# employee = {
#     "raj": 30000,
#     "ram": 35000,
#     "tushar": 40000,
#     "kiran": 45000,
#     "karan": 50000,
#     "roshan": 55000,
#     "pratik": 60000,
# }

# iterate name of employy > 40k (not include 40k)
# name_em = []

# for name, salary in employee.items():
#     if salary > 40000:
#         name_em.append(name)
# print(name_em)

# # > 40k < 51k
# name_e = []

# for nam, sal in employee.items():
#     if sal > 40000 and sal < 51000:
#         name_e.append(nam)
# print(name_e)

# # salary < 47k list names
# # salary > 47k list names

# gt = []
# ld = []

# for na, sa in employee.items():
#     if sa > 47000:
#         gt.append(na)
#     else:
#         ld.append(na)
# print(gt)
# print(ld)

# employee = {
#     "raj": 30000,
#     "ram": 35000,
#     "tushar": 40000,
#     "kiran": 45000,
#     "karan": 50000,
#     "roshan": 55000,
#     "pratik": 60000,
# }

# salary < 50k increment 20% - value(salary) update

# print(employee)

# for nam, sal in employee.items():
#     if sal < 50000:
#         dis = 20 / 100 * sal
#         updated_salary = dis + sal
#         employee[nam] = int(updated_salary) # updated to the orignal dictionary

# print(employee)


# employee = {
#     "raj": 30000,
#     "ram": 35000,
#     "tushar": 40000,
#     "kiran": 45000,
#     "karan": 50000,
#     "roshan": 55000,
#     "pratik": 60000,
# }
# print(employee)
# # sal < 50k increment 10%
# # sal >= 50k increment 5%

# # iteration using for in loop
# for nam, sal in employee.items():
#     if sal >= 50000:  # >= 50k
#         dis = 5 / 100 * sal
#         new_price = sal + dis
#         employee[nam] = int(new_price)  # update the orignal dictionary
#     else:
#         dis1 = 10 / 100 * sal  # < 50k
#         new_price1 = dis1 + sal
#         employee[nam] = int(new_price1)

# print(employee)


# today topic - if elif else -4
# explain - if i want to run only one condition to run from multiple conditions

# if i want to run only one from these
# if cond1 :
# if block
# elif cond2:
# elif block
# elif cond3:
# elif block
# else:
# else block

# -- ex - 1
# num = int(input("enter a number - "))
# if num > 0:
#     print(f"{num} is positive number")
# elif num < 0:
#     print(f"{num} is negative number")
# else:
#     print(f"{num} is zero")

# -- ex - 2
# wap to check child adult senior based on the age.

# num = int(input("enter age - "))

# if num < 20 and num >= 1:
#     print("you are an child")
# elif num < 50:
#     print("you are an adult")
# elif num < 99:
#     print("you are a senior")
# else:
#     print('you are a god')
