# range and operation in python -
# topic -
# range - range is used to generate whole number(1,2,3,4,5,6,7,8,9,10)
# the default value of start  = 0 and default value of step value is 1
# revision -

# iterable - str,list,tuple - collection of data

# for var in iterable:
# body

# example 1. -
student = [
    "ketan ramdev patil",
    "rajiv keshav raut",
    "ram vidrup singh",
]

formatted_students = []

for name in student:
    students = name.split()  # it will split the string based on the white space between
    new_list = f"{students[0][0]}.{students[1][0]}.{students[2]}".title()
    formatted_students.append(
        new_list
    )  # it will add the data to the list at the end of the list
# print(formatted_students)  # ['K.R.Patil', 'R.K.Raut', 'R.V.Singh']

# example 2 -

students_names = ["pranav", "namdev", "vijay", "vasudev"]

new_stu_names = {}  # empty variable to store dict data

for names in students_names:
    length = len(names)
    new_stu_names[names] = length
# print(new_stu_names)  # {'pranav': 6, 'namdev': 6, 'vijay': 5, 'vasudev': 7}


# today's topic Range  -
# syntax -
# var = range(start value,stop value,step value)
# range is a data type of python it is used to generate sequence of whole number - 

# 10 to 100 number(sequence) - range()

# how to use it -
# range(1, 11, 1)  # [1,2,3,4,5,6,7,8,9,10]

# for i in range(11, 21, 1):
# print(i)

# example 1 -
for s in range(10, 0, -1):
    print(s)

# example 2 - wap to print numbers from 50-100

# for i in range(50, 101, 1):
# print(i)

# for s in range(100, 49, -1):
# print(s)

# l = [] # empty list to store data
# for j in range(1, 11, 1):
# l.append(j)

# print(l)  # when i dont use space that means i am out of the for loop
# c = set()
# for z in range(21, 10, -1): #
#     c.add(z)

# print(c)

# e = []
# for s in range(2, 11, 2): # even numbers
#     e.append(s)

# print(e)

# o = []
# for h in range(11, 0, -2): # odd numbers
#     o.append(h)

# print(o)

# x = {}
# for i in range(11, 21, 1):
#     x[i] = i**2

# print(x)

# s = {}
# for o in range(2, 11, 2):
#      s[o]= o**3

# print(s)
