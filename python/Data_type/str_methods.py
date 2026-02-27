# str methods in python

# revision -

cls = "hello world world"  # object
a = cls.upper()
c = cls.replace(
    "world", ", i am the king of this world", 1
)  # the "1" means only one word("world") will be replaced by the new word in the string , the default will replace all the word with ("world") in that string
# print(a)
# print(c)

# -- def (define) :  The def keyword in Python is used to define a function. The word "def" is short for "define"

# example 2.

institute = "i am the king of this world"
# print(institute.split())  # it splite the word based on the white space
# print(institute.split(sep="o"))  # it splite the word based on the word "o" and it will replace the "o" with white space

# example 3.

# lstrip - will remove white space and character from left side
# rstrip - will remove white space and character from right side

name = " vaibhav "
name1 = "vaibhav"
# print(name)
# print(name.strip()) #  to remove the white space
# print(name.lstrip())
# print(name.rstrip())
# print(name1.lstrip("v"))
# print(name1.rstrip("v"))
# print(name1.strip("v"))  # to remove the word "v"

# example 4.

sr = "hello world"
# print(sr.startswith("h"))  # true - if the string start with "h"
# print(sr.endswith("d"))  # true - if the string end with "d"
# print(sr.startswith("e"))  # false
# print(sr.endswith("o"))  # false
# print(sr.startswith("l", 2))  # true - you can define where the string should start using indexing
# print(sr.endswith("o", 0,-3))  # true - you can define where the string should end using indexing

# example 5.

ml = "hello world"

# print(ml.isalpha())  # false - because the string has white space
# print(ml.isspace())  # false - because the string has charaters also
# print(ml.isspace())  # false - because the string has charaters also

# example 6.

# student = ["ketan", "kusha", "shyam", "kapila", "ketu"]

# for name in student:  # for loop in python -
#     if name.startswith("k"):
# print(name) # it will only print the word which start with "k"

# example 7.

# x = ["ketan", "42", "kusha", "shyam", "43", "kapila", "ketu", "23"]

# for num in x:
#     if num.isnumeric():
# print(num)

# example 8.

# student = ["vaibhav patil", "raj raut", "ketan patil", "shyam patil"]

# for name in student:
#     print(name.title())

# example 9.

nam = "fortune"
# print(nam.center(40,"*"))
# print(nam.center(40,"-"))

# example 10.

name = "i am the king of this world"
print(name.split())  # it will split the word based on the white space

# example 11.
os = ["i", "am", "the", "king", "of", "this", "world"]
print(" ".join(os))
print("-".join(os))


# test -

# 1.
s = "hello world"
print(s.upper())

# 2.
s1 = "PYTHON PROGRAMMING"
print(s1.lower())

# 3.
s2 = "python is fun"
print(s2.capitalize())

# 4.
s4 = "data science"
print(len(s4))

# 5.
s5 = "This is a bad idea"
print(s5.replace("bad", "Good"))

# 6.
s6 = "hello world"
print(s6.index("o"))

# 7.
s7 = "hello world"
print(s7.count("l"))

# 8.
s8 = "Python123"
print(s8.isalpha())

# 9.
s9 = "123456"
print(s9.isnumeric())

# 10.
s10 = "apple,banana,mango"
print(s10.split(","))

# 11.
s11 = ["Python", "is", "fun"]
print("".join(s11))

# 12.
s12 = " hello world "
print(s12.strip())

# 13.
s13 = "hello world"
print(s13.startswith("hello"))

# 14.
s14 = "hello world"
print(s14.endswith("world"))

# 15.
s15 = "python"
print(s15.title())

# 16.
s16 = "abcdef"
print(s16[::-1])

# 17.
s17 = "hello world"
print(s17[6:])

# 18.
s18 = "python is fun"
a = s18.split()
print(a)
print("-".join(a))

# 19.
s19 = "123"
print(int(s19))
print(type(int(s19)))

# 20.
s20 = 234
print(str(s20))
print(type(str(s20)))

# end -

#  List in python

#  topic --
#   1. str (string)
#   2. methods
#   3. List - it is a collection of data types which are order(sequece(1,2,3)) they have index numbers, using index number you can access the character/value from that string/list/tuple/set/frozenset/dictionary.

# revison  -

# var = "char"
# print(var[3])  # oparation related this object is stored in the blueprint/class

# # every data type has its own blueprint/class in python

cls = "hfsdnl safk"
# print(cls.upper())

# print(cls.replace("dn","ll"))

# print(cls.split(sep="a"))
# print(cls.strip()) # will remove your white space
# print(cls.strip("h")) # it will remove the word "f"
# print(cls.rstrip("h")) # it will renove space/charactor from right side
# print(cls.lstrip("k")) # it will renove space/charactor from left side
# print(cls.startswith("h"))  # it will return true if the string start with "h" otherwise false
# print(cls.startswith("s", 2))  # i can define when the should start also
# print(cls.endswith("k")) # it will return true if the string end with "k" otherwise false

# student = ["ketan", "kusha", "shyam", "kapila", "ketu"]
# for name in student:  # for loop in python
#     if name.startswith("k"):
#         print(name)

# x = ["ketan patil", "kusha raut", "shyam", "kapila singh", "ketu singh"]

# for n in x:
#     if n.isnumeric():
#         print(n)

# for name in x:
#     print(name.title())

# name = "vaibhav"
# print(name.center(29,"-")) # it will center string in what ever width you give it to print

# p = "jksd hsdfn asdnf"
# list = p.split()  # list type
# print(type(list))
# print(list)
# line = " ".join(list) # string type -- give what you want it to add whitespace with
# line = "-".join(list) # string type -- give what you want it to add whitespace with
# line = "::".join(list) # string type -- give what you want it to add whitespace with
# print(type(line))
# print(line)

# name = "python"
# print(name * 3)

# task --

# 1.
s = "hello world"
print(s.upper())

# 2.
s = "PYTHON PROGRAMMING"
print(s.lower())

# 3.
d = "python is fun"
print(d.capitalize())

# 4.
x = "data science"
print(len(x))

# 5.
i = "This is a bad idea"
print(i.replace("bad", "good"))

# 6.
p = "hello world"
print(p.index("o"))

# 7.
h = "hello world"
print(h.count("l"))

# 8.
m = "Python123"
print(m.isalpha())

# 9.
f = "123456"
print(f.isnumeric())

# 10.
sk = "apple,banana,mango"
print(sk.split(","))  # it will return a list type with a comma as a separator
print(type(sk.split(",")))

# 11.
sd = ["python", "is", "fun"]
print(type(sd))
print(" ".join(sd))  # it will return a string type with a space as a separator
print(type(" ".join(sd)))  # it will return a string type with a space as a separator

# 12.
we = " hello world "
print(we.strip())

# 13.
sd = "hello world "
print(sd.startswith("hello"))

# 14.
sd = "hello world "
print(sd.endswith("world"))

# 15.
py = "python programming"
print(py.title())

# 16.
sx = "abcdef"
print(sx[::-1])

# 17.
hj = "hello world"
print(hj[5::1])

# 18.
hj = "python is fun"
sd = hj.split()
print("-".join(sd))

# 19.
aer = "2343"
print(type(aer))
print(int((aer)))
print(type(int(aer)))

# 20.
aer = 2343
print(type(aer))
print(str((aer)))
print(type(str(aer)))


# timeframe -  1:18:15