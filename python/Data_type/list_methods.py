# list methods in python -
# list
# methods

# - list is mutable , you can change it

# revision

i = [11, 3, 23, 23, 2, 32]

# index
# forward | posiitve
# reverse | negative

# indexing -
#    var[index]

# slicing : multiple
#    var[si :ei : sv]

# Nested list  - explain - a list that contains other lists as its elements

numbers = [12, 34, 34, [234, 343, 344, 342], 234, 34, 34]  # list of list

# example 1. - list methods in python

students = [
    "pranav",
    "shyam",
    "ketan",
    ["pravin", "parik", ["rishabh", "jain", "rameshwar", "kumari"], "ketan", "ketu"],
    "kusha",
    "kapila",
]

# example 1 .
# print(students[3][2][-3])

# example 2.
# print(students[3][-1][2:])

# example 3.
string1 = students[3][2][1]  # rishabh
string2 = students[3][2][-1]  # kumari

word = [string1, string2]
# print(word)

# example 4.
# print(students[3][2][0:4:3])
# print(students[3][1:5:3])


# list method  - methods in python

# to add data into list


# 1.append -
# 2.insert -
# 3.extend -

# 1. append - it will add the data to the end of the list
# l = [34, 3, 434, 3, 4, 34, 3, 4, 2.3]
# l.append(23)
# print(l)

# # 2. insert - is a predifined method of list it takes two arguments index and data and it add's the data before the index you gave

# num = [
#     12,
#     34,
#     34,
#     34,
#     43,
#     2,
#     32,
# ]
# num.insert(4, 25)
# print(num)

# # 3. extend - it takes a iterable object and add's it's elements to the end of the list
# num1 = [23, 23, 23]
# num2 = [33, 2, 66] # iterable object

# num1.extend(num2)  # num1 = num1 + num2
# print(num1)

# name = [23,2,4,2,4]
# s ="kunm" # iterable object
# name.extend(s)
# print(name) # [23, 2, 4, 2, 4, 'k', 'u', 'n', 'm']

# diffrence between append and extend  - append add objects to the end of the list and extend add iterable elements to the end of the list

# --

x = [10, 20, 30]
l = [2, 3, 4]
# x.append(l) # it will add the x object to the x
x.extend(
    l
)  # it will add the iterable object's elements of the l to the x at the end of the list
# print(x)

# --

numbers = [10, 20, 30, 40, [11, 22, 33, [1, 2, 3, 4, 5], 44, 55, 66], 50, 60, 70]

# numbers.append(80)

# numbers.insert(-2, 51) -

# numbers[4].append(77)

# [10, 20, 30, 40, [11, 22, 33, [1, 2, 3, 4,5], 44, 55, 66, 77], 50, 60, 70]
# numbers[4][3].insert(2, 22)

# [10, 20, 30, 40, [11, 22, 33, [1, 2, 22, 3, 4], 44, 55, 66], 50, 60, 70]
# numbers[4][3].append(6)

# [10, 20, 30, 40, [11, 22, 33, [1, 2, 3, 4, 5, 6], 44, 55, 66], 50, 60, 70]

# print(numbers)

# --
# update data - by using

# indexing - for single element
# syntax - var[index] = updated value

# slicing - for multiple elements
# syntax - var[start-index : end-index : step value] = iterable

# example 1. - to update single element
l = [10, 20, 333, 40, 50]
l[2] = 30  # [10, 20, 30, 40, 50]
# print(l)

# example 2. -- to add more elements to the list
o = [11, 22, 33, 44, 55, 66, 76]
o[2:-3:1] = [23, 99, 77]
# print(o)

# example 3.
course = ["web", "ds", "ml", "da", "ws"]

# course.insert(0, "web development")
# course[1:-1:1] = ["data science", "machine learning", "data analytics"]
# print(course)


# --
# how to delete data

# remove() - it will remove the element based on the value and return none
# syntax - var.remove(data/value)

# pop() - it will remove the element based on the index and return the deleted/removed element/value
# syntax - var.pop(index)

# clear()
# syntax - var.clear() - to clear the list

# del - it was a keyword, it will delete the element based on the index
# syntax - del var[index]
# del var[start:end:step]

# --

# example 1.
l = [23, 3, 43, 1, 6]
l.remove(3)  # [23, 43, 1, 6]
# print(l)

# example 2.

ld = [43, 23, 3, 43, 1, 6]
ld.pop(0)
# print(ld)
# timeframe - 1:23:49

# example 3.
pased = ["ajau", "vaibhav", "rohit", "yash"]
failed = ["payal", "siddhi", "sakshi", "rutuja", "pranav"]
# failedList = failed.pop(2)  # pop will pass the removed value into failedList.
# pased.append(failedList)
pased.append(failed.pop(2))  # pop will pass the removed value into failedList
# print(pased)
# print(failed)

# example 4.

ll = [12, 23, 45, 7, 8, 3]
ll.clear()  # to clear the list
# print(ll)

# example 5.
wl = [12, 23, 45, 7, 8, 3]
del wl[2]  # to delete the element based on the index
del wl[2:-2:1]
# print(wl)

# example 6.
lw = [12, 23, 45, 7, 23, 8, 3, 3.3, "sdlf"]
# print(lw.index(23))
# print(lw.index(23, 3))

# example 7.
l1 = l.copy()
# print(l1)

# example 8.
l2 = [12, 23, 45, 7, 8, 3]
l2.reverse()
# print(l2)

# example 9.
l3 = [12, 23, 45, 7, 8, 3]
l3.sort()
print(l3)
