# comprehention -
# explain -provide a concise and efficient way to create new sequences (lists, sets, and dictionaries) from existing ones, often in a single line of code

# types - list comprehension , set comprehension , dictionary comprehension

numbers = [1, 2, 3, 4, 5, 6, 7]  # iterable

# normal way
# square = []

# for num in numbers:
#     sq = num**2
#     square.append(sq)

# print(square)

# normal way
# square = []

# for num in numbers:
#     if num % 2 == 0:
#         sq = num**2
#         square.append(sq)

# print(square)

#  normal way
# square = []
# x = []

# for num in numbers:
#     if num % 2 == 0:
#         sq = num**2
#         square.append(sq)
#     else:
#         cu = num**3
#         x.append(cu)

# print(x)


# using list comprehention

"""
new_list = [exp for var in iterable] 
new_list = [exp for var in iterable if condition]
new_list = [exp1 if condition else exp2 for var in iterable]

new_set = {exp for var in iterable}
new_set = {exp for var in iterable if condition}
new_set = {exp1 if condition else exp2 for var in iterable}

new_dict = {key:exp for var in iterable}
new_dict = {key:exp for var in iterable if condition}
new_dict = {key:exp1 if condition else exp2 for var in iterable}

"""

numbers = [1, 2, 3, 4, 5, 6, 7]  # iterable

square = [num**2 for num in numbers]
print(square)

# ----------------------------------------------------------

"""
new_list = [exp for var in iterable if condition] 

"""

numbers = [1, 2, 3, 4, 5, 6, 7]  # iterable

square = [num**2 for num in numbers if num % 2 == 0]
print(square)

# ----------------------------------------------------------

"""
new_list = [exp1 if condition else exp2 for var in iterable]

"""

numbers = [1, 2, 3, 4, 5, 6, 7]  # iterable

square = [num**2 if num % 2 == 0 else num**3 for num in numbers]
print(square)

# ---------------------------------------------------------

marks = {"kunal": 78, "pavan": 34, "rahul": 90, "vijay": 21}
# print list of name of student =>uppercase
# print list of name of passed student
# ["KUNAL", "pavan", "RAHUL", "vijay"] pass in uppercase else lowercase


#-------------------------------------------------------------
# dict comperehension 

numbers = [1, 2, 3, 4, 5, 6, 7]  # iterable

square = {num: num**2 for num in numbers}
print(square)

#-------------------------------------------------------------

# even_square ={ k:v for num in numbers if num %2 == 0}