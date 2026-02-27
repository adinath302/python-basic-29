# range in python -
# topic -
# iteration -
# for loop -
# 35 keywords in python

# revision - dict methods 

# square = {1:2,2:3,3:4}
# var[key] => value
# print(square[2]) # 3

# var[key] = value
# square[4] = 5 # to add key and value
# var.pop(key) # to delete key and value
# square.pop(2)

# values => all values
# keys => all keys
# items => key and value pairs

# get() # to get the value from the key
# popitem() # remove the last key and value pair

# update # to add multiple(dict) value
# clear() # to remove the all key and vlue from the dict
# fromkeys() # to create a new dict with multiple keys
# setdefault() # to set the default value for the key

# student = ["harsh", "ketan", "kusha", "shyam", "kapila", "ketu"]
# res = dict.fromkeys(student, 0)
# print(res)

# setdefault -

# iteration - 

# [1,2,3,4,4,5] - this is 'iterable'
# the process of extracting the values from the box is called 'iteration'
# 'for loop' is used to iterate all element from an 'iterable'

# syntax -

# for var in iterable :
# body/block

#  example

# numbers = (10, 23, 34, 45, 56, 67)
# print("start")
# for num in numbers:
#     print(num)

# print("end")

# name = 'vaibhav'
# for char in name :
#     print(char)

dct = {"name": "kiran", "age": 23, "city": "pune"}
# for d in dct:
#     print(d, dct[d])   # variable name [key] - to get value

# all_values = dct.values()  # to get the values from an dictionary
# for i in all_values:
#     print(i)

# for i in dct.values():  # using this method you can get the vlaues from the dictionary
#     print(i)

# items  -

# print(
#     dct.items()
# )  # dict_items([('name', 'kiran'), ('age', 23), ('city', 'pune')]) it's iterable and can be used in for loop

# for i,j in dct.items(): # it return key and value inside tuple
#     print(i)
#     print(j)

# example -

# sd = [2, 3, 4, 5, 6, 7, 8]
# for s in sd:
#     print(f"square of {s} is {s**2}")

# list of square of all number

we = [2, 3, 4, 5, 6, 7, 8]

square_list = []  # first create a empty list

for s in we:
    square = s**2
    square_list.append(square)

# print(square_list) # [4, 9, 16, 25, 36, 49, 64]

# example  -

# write a p to print dict of cube of all number

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

cube_dict = {}

for c in num:
    cube = c**3
    cube_dict[c] = cube  # variable name[key] = value this used to create a dictionary

# print(cube_dict)  # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729}

# wap to print dict of selling value

vivo = {"vivo v20": 20000, "vivo v21": 30000, "vivo v22": 40000, "vivo v23": 50000}

# selling_price = {}
# discount = 10

# for k, v in vivo.items():  # key(k) value(v) get the key and value from the dict
#     sp = v * discount / 100
#     dp = v - sp
#     selling_price[k] = dp

# print(selling_price)
 
 
# employee salary data
employee_salary = {
    "rajesh": 40000,
    "kunal": 50000,
    "shyam": 60000,
    "prathmesh": 70000,
    "digesh": 80000,
}

# increment 15% every employee

increment_salary = {}

for k, v in employee_salary.items(): # for in use to exact the key and value
    increment = v * 15 / 100  # 15 percent of the salary
    new_salary = v + increment
    increment_salary[k] = new_salary

print(increment_salary)
