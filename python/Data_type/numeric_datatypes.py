# data types in python

# 1. numeric data types
#  -- explain - data types will help you to identify what kind of data variable is holding & what operations can be performed on that data. data types are classified into two types in python one is fundamental and collective data types.

# var = value # variable declaration with value assignment

# num = 30
# name = "raj"

# predefined data types in python

# 1. fundamental data types  ⤵        |    # 2. collective data types ⤵ (collection/list of data)
#                                      |
# a. numeric data types             |     # a. list data type (list)
#  1. int                          |     # b. tuple data type (tuple)
#  2. float                        |     # c. set data type (set)
#  3. complex                      |     # d. frozenset data type (frozenset)
# b. string data type (str)         |     # d. dictionary data type (dict)
# c. boolean data type (bool)       |     # e. range data type (range)


# numeric data types ⤵

# 1. int - integer data type - it is used to stored whole numbers (positive & negative both(1,-1,0)) - whole numbers means without decimal point
# example -
# num = 10  # integer data type

# 2. float - it is used to stored decimal number (positive & negative both (1.5,-1.5,0.0)) - decimal numbers means with decimal point
# example -
# num - 10.4 # float data type

# 3. complex number - it is used to stored complex numbers (numbers with real & imaginary parts) - it is represented by "a + bj" where "a" is real part and "b" is imaginary part the letter "j" (or "J") is used as a suffix to denote the imaginary part of a complex number. It is equivalent to the mathematical imaginary unit i, where \(j^{2}=-1\) (or \(i^{2}=-1\)). 1 - real part of the complex number can be int or float & 2 - imaginary part of the complex number must be decimal or float (".")
# example -
# num = 5 + 9j  # complex data type
# print(num.real)  # to get the real part of the complex number
# print(num.imag)  # to get the imaginary part of the complex number
# print(type(num))

# ____________________________________________

# balance = 1500  # int data type
# print(type(balance))

# height = 4.5  # float data type
# print(type(height))

# c = 4 + 5j  # complex data type
# print(type(c))  # to check the data type
# print(c.real)  # to get the real part of the complex number
# print(c.imag)  # to get the imaginary part of the complex number
# num = c.real
# print(num)

#  integer -
#    binary (base 2) - 0,1
#    octal (base 8) - 0 to 7
#    decimal (base 10) - 0 to 9
#    hexadecimal (base 16) - 0 to 9 and a to f

# binary number-
# value => 0 and 1
# var = 0bvalue # binary representation starts with "0b"

# num = 0b1010  # binary representation of 10
# print(num)

# num = 20
# print(bin(num))  # to convert decimal to binary

# octal number -
# value => 0 - 7
# var = 0ovalue  # octal representation starts with "0o"

# num = 0o24  # octal representation of 20
# print(num)
# num = 20
# print(oct(num))  # to convert decimal to octal

# decimal number -

# var = value # decimal representation

# value ===> 1-9

# hexadecimal number -

# value => 0-9 and a-f

# var = 0xvalue  # hexadecimal representation starts with "0x"

# example -

n = 49  # hexadecimal representation of 49
print(hex(n))  # to convert decimal to hexadecimal

# example -
# c = 10 + 10j
# c = 10.7 + 10j
# c = 0b1010 + 10j
# c = 0o12 + 10j
# c = 0x12 + 10j

# print(c)

c = 10 + 10j

print(c)  # complex number representation
print(type(c))  # to check the data type