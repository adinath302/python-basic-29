# Data type in python -

# topic to cover --

# 1. string data type (str)
#  - indexing
#  - slicing

#  explain - it is collection of character within single('') or double quotes ("") or triple quotes(''' ''').

# example
# 1.
# name = "ketan"
# print(type(name))

# # 2.
# x = "12.54"  # anything inside single/double/triple quotes is called string data type
# print(type(x))

# # 3.
# num = 199  # number(int) data type
# print(type(num))

# ---

# topic - indexing -
# explain - in python if i use a string python will assign index number on each of that character in that string. index numbers strarts from 0 to the length of the string. index numbers are only on that data types which are order(sequece(1,2,3)) they have index numbers, using index number you can access the character/value from that string/list/tuple/set/frozenset/dictionary.

# -- sting is an unmutable data type after initialization in object
# -- data types which are order(sequece(1,2,3)) they have index numbers

# example - 2 tyepes of indexing -

#         ⬅️ negative indexing / reverse indexing <-
#                  -6  -5  -4  -3  -2  -1
#  left             r   a   j   e   s   h            right
#                   0   1   2   3   4   5
#         -> positive indexing / forward indexing ➡️

# for example - positive indexing
# x = "rajesh"
#  r  a  j  e  s  h
#  0  1  2  3  4  5

# how to access char.(character) from string  =
x = "elephant"
# indexing : if you want to access single character("p"),("h")
# slicing : if you want to access multiple charater("ele"),("phant")

# indexing -
# example 1
x[3]  # x is variable name and 3 is positive index number
# print(x[3]) # print will print the character at index number 3

# example 2
x[-2]  # x is variable name and -2 is negative index number
# print(x[-2]) # print will print the character at index number -2

# slicing --
# explain - it creates a new string(substring) without modifiying the original string. as string in python are immutable data type. they can not be changed.
# stepvalue -> forward - +value
#              reverse - -value

# example 1 -

# syntax -x[start,end,step] - step value - diffrence between start and end value , and the default value is 1.
# x[start:end:step] - slicing syntax

x[1:3:1]
# print(x[1:3:1])
x[1:5:1]
# print(x[-5:-1:1])
# print(x[-2:-1:1])

# tasks - 1

y = "i am the king of this world"
# print(y[-1])
# print(y[-15])
# print(y[10])

k = y[9]
t = y[-10]
w = y[-5]
to = k + t + w  # concatenation of string
# print(y[9]+y[-10]+y[-5]) # another method
# print(to)

# task - 2

name = "raajeshkumar"

name[1:4:1]
# print(name[1:4:1])  # aaj

# name[0:8:1]
# print(name[0:7:1])  # raajesh

nm = name[0:7:1]
# print(nm)  # raajesh

ok = name[7:-1:1]
# print(ok)  # kuma

ra = name[-1:-4:-1]
# print(ra)  # ram

ku = name[7:12:1]  # kumar
# print(ku) # kumar

# task - 3

qk = "python programming language"

a = qk[:6:1]
# print(a)  # python

ar = qk[-27:-20:1]  # reverse indexing
print(ar)  # python

b = qk[7:19:1]
# print(b)  # programming

br = qk[-20:-9:1]  # reverse indexing
# print(br) # programming

c = qk[19::1]  # the blank space represent the end of the string
# print(c)  # language

cr = qk[-9::1]  # reverse indexing
# print(cr) # language

# default value for step value is 1

# end
