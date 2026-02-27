# todays topic - file handling
# process -
# open - open the file
# operation - read, write
# close - close the file
# ----------------------------------------
# f is a file pointer
# ----------------------------------------

# f = open('File & Exception Handling/file handling/demo1.txt','r')
# print(list(f))
# print(list(f))

# to get the needed file path
import os as os

f1 = os.getcwd()

# os.chdir("")
# print(os.getcwd())

# reading -
"""
read
readline
readlines

"""
# ----------------------------------------
# read

# f = open('File & Exception Handling/file handling/demo1.txt','r')
# data = f.read()
# print(data)

# f = open('File & Exception Handling/file handling/demo1.txt','r')
# data = f.read(10)
# print(data)

# ----------------------------------------
# readline - it will only read one line

# f = open("File & Exception Handling/file handling/demo1.txt", "r")
# l1 = f.readline()
# print(l1)

# l2 = f.readline()
# print(l2)

# l3 = f.readline()
# print(l3)
# ----------------------------------------
# readlines - return list of all lines

# f = open("File & Exception Handling/file handling/demo1.txt", "r")
# l1 = f.readlines()
# print(l1)

# ----------------------------------------

# f = open("File & Exception Handling/file handling/demo1.txt", "r")
# l2 = f.read()
# print(l2)


# ----------------------------------------

# f = open("File & Exception Handling/file handling/demo1.txt", "r")
# l3 = f.readline()
# print(l3)  # the

# fi = f.tell()  # current position of cursor
# print(fi)
# # seek method - to change position
# f.seek(0)

# l31 = f.readline()
# print(l31)

# data = f.read()
# print(data)

# fi = f.tell()  # current position of cursor
# print(fi)

# ----------------------------------------
""" write - on data - w(write),a(append),x(exclusive) mode of doing it """

# it override the previous data with new data
# if the file you gave is not available it will create it and  write the data , and if the file is available it will override the previous data(the previous data will removed)
# -------------------------------------------------

# write method(w) 1
# f = open("File & Exception Handling/file handling/demo1.txt", "w")
# f = open(
#     "File & Exception Handling/file handling/demo5.txt", "w"
# )  # this will create a new file and write the data
# f.write("hello it's new data ")  # it takes string data and adds to the file
# f.close()

# ----------------------------------------
# append(a) -
# it will add the data at the end of the file (previous data)
# will not override the previous data
# also in this case if the file is not available it will create a new file and write the data

# f = open("File & Exception Handling/file handling/demo1.txt", "a")
# f.write("hello new data form append method")

# ----------------------------------------
# exclusive(x) -
# it will only create a new file , if the file is present it will throw an error


# f = open("File & Exception Handling/file handling/demo6.txt", "x")
# f.write("hello this is an exclusive file")

# ----------------------------------------
# write lines - method 2

# he writelines() method is used to write a list of strings (or any iterable like a tuple) to a file all at once

# f = open("File & Exception Handling/file handling/demo1.txt", "a")
# f.writelines(['hello user \n ', 'thank you \n', "welcome\n"])
# ----------------------------------------

# f = open("File & Exception Handling/file handling/demo1.txt", "w")
# print(f.readable())  # it will show if the file is readable or not in bool value
# print(f.writable())  # it will show if the file is writeble or not in bool value

# ----------------------------------------
""" + mode (combaining 2 or more modes) """

# f = open("File & Exception Handling/file handling/demo1.txt", "w+")
# print(f.readable())  # it will show if the file is readable or not in bool value
# print(f.writable())

# f = open("File & Exception Handling/file handling/demo1.txt", "r+")
# print(f.readable())  # it will show if the file is readable or not in bool value
# print(f.writable())

# f = open("File & Exception Handling/file handling/demo1.txt", "a+")
# print(f.readable())  # it will show if the file is readable or not in bool value
# print(f.writable())


# ----------------------------------------
"""
open 

read methods - read , readline, readlines

write methods  - write , writelines 

mode  - r(read) , w(write) , a(append) , x(exclusive) , + modes

close

"""
# ----------------------------------------
# example -

# f = open("File & Exception Handling/file handling/prac1.txt", "a")
# while True:
#     name = input("enter your name : ")
#     if name == "stop":
#         break
#     f.write(f"{name}\n")
# f.close

# ----------------------------------------
#

f = open("File & Exception Handling/file handling/prac2.txt", "r")
for line in f:
    l = line.split()
    obt = 0
    for marks in l[1:]:
        obt = obt + int(marks)
    per = obt / len(l[1:] * 100)
    print(f"{l[0]} : {per}")

# ----------------------------------------
# ----------------------------------------
# ----------------------------------------
# ----------------------------------------

# timeframe - 32:39
