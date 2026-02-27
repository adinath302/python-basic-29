# data type in python
# set
# > methods
# tuple
# frozenset

# revision -
# summary -
students = {}  # if it's empty it's dictionary
students = {"om", "pranav", "ketan", "shyam", "kusha"}  # it's a set
students = set()  # it's a empty set

# set is a unordered,mutable,heterogeneous collection of elements only , duplicate value is not allowed in it

# methods - add, remove, pop, discard, clear,del, intersection,difference,symmetric_difference

test1 = {1, 2, 3, 4, 5}
test2 = {1, 3, 2, 9}
test3 = [3, 4, 5, 6]

# print(test1.intersection(test2, test3))  # to get the common values from test1 and test2 - {5}
# print(test1.difference(test2))  # to get the values from test1 which is not present in test2 - {4, 5}
# print(test2.difference(test1)) # to get the values from test2 which is not present in test1 - {9}
# print(test1.symmetric_difference(test2))  # to get the values which are not present in both test1 and test2 - {4, 9}

# --
# intersection update -

# s1 = {1, 2, 3, 4, 5, 11, 12, 13}
# s2 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# s3 = {3}
# s1.intersection_update( s2)  # it will keep only elements/data/values which are common in both s1 and s2
# s2.intersection_update(s1)  # it will keep only elements/data/values which are common in both s2 and s1
# s1.difference_update(s2)  # it will keep only data which is not present in both s1 and s2, it will remove the common data from both s1 and s2
# s1.symmetric_difference_update(s2) # it will remove the data which is common in both s1 and s2 and it will add the data which is not common in both s1 and s2
# print(s1)

# --
# subset and superset

# example - if the s1 contain all the values of s2 then s1 is a superset of s2

# s1 = {1, 2, 3, 4, 5}  # s1 is superset of s2 because
# s2 = {3, 4, 3}  # s2 is subset of s1

# print(s2.issubset(s1))  # true
# print(s1.issuperset(s2))  # true
# print(s2.issuperset(s1))  # false

# --
# isdisjoint - if both set's values are not common then it return true otherwise false
# s1 = {1, 2, 3, 4, 5}
# s2 = {6, 7, 8, 9, 10}
# s3 ={6, 7, 8, 9, 10}
# s2.isdisjoint(s1) # true - not common values
# s2.isdisjoint(s3) # false - common values
# print(s2.isdisjoint(s1))

# --
# union - it will return a new set with the union of both s1 and s2
# s1 = {1, 2, 3, 4, 5}
# s2 = {6, 7, 8, 9, 10}

# s3 = s2.union(s1) # it will return the union of both s1 and s2
# # print(s3)

# # --
# # update - it will updaate s1 wiht the values of s2
# s1 = {1, 2, 3, 4, 5}
# s2 = {6, 7, 8, 9, 10}

# s1.update(s2) # it will update the s1 with the values of s2
# print(s1)

# --
# tuples  -
# explain  -  it is ordered, immutable, heterogeneous collection of elements , where duplicates are allowed.

# student = ("hi",) "," to create tuple with a single value

# syntax -
# vars = (1,2,3,4,5,6,7,8,9,0)
# print(type(vars)) # type is tuple

# s1 = (2, 3, 4, 5, 6, 6, 7)
# print(s1[2]) # indexing
# print(s1[1:4:1]) # slicing


# list is mutable tuple is immutable
# syntax [] syntax ()

# packing and unpacking

# unpacking
t = (11, 22, 33)  # packed tuple
x, y, z = t  # tuple unpacking
print(x)
print(y)
print(z)

# packing
n1 = "Adinath"
n2 = "Gaware"
n3 = "Software developer"
n4 = "trader"
n5 = "entrepreneur"
t = n1, n2, n3, n4, n5  # this is packing inside a tuple
print(t)
print(type(t))

# mutable and immutable -
t1 = (1, 2, 3, 4, 5)
# memory utilization of tuple -
# explanation - if the objects are same and immutable then it will stored in the same memory location. with diffrent refrence name .
# example -

t2 = (1, 2, 3, 4, 5)
t3 = (1, 2, 3, 4, 5)

# print(id(t3))
# print(id(t2))

# if mutable(list) - it will stored in diffrent memory location with diffrent refrence name
# example -
l1 = [11, 22, 33, 44]
l2 = [1, 2, 3, 4]
l3 = [11, 22, 33, 44]

# print(id(l1))
# print(id(l2))
# print(id(l3))

# data type comparison -

# list                                tuple
# mutable                             immutable
# packing possible                    packing and unpacking possible


# --
# frozenset --
# explain - it is unordered, immutable, heterogeneous collection of immutable elements where duplicates are not allowed.

# example -
# syntax -
# fs =  frozenset({11,22,3.3,"hello",(1,2,3,4,5),11,11})
# print(fs)
# print(type(fs))

# example 2.

f1 = frozenset({1, 2, 3, 4, 5, 7})
f2 = frozenset({1, 2, 3, 4, 5, 6})
# print(f1.difference(f2))  # frozenset({7})
# print(f1.intersection(f2)) # frozenset({1, 2, 3, 4, 5})
# print(f1.isdisjoint(f2)) # false
# print(f1.issubset(f2)) # false
# print(f1.union(f2))  # return a new frozenset frozenset({1, 2, 3, 4, 5, 6, 7})
# print(f1.symmetric_difference(f2))  # frozenset({6, 7})
# print(f1.issuperset(f2)) # False


# -- before using data
# duplicate allowed or not
# orderd or unordered
# mutable or immutable 
# 