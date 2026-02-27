# set in python
# methods

# l = [12, 33, 44, 55, 66]
# access
# print(l[4])
# print(l[1:-1:1])

# add
# l.append(55)
# l.insert(1,55)
# l.extend([55,44,33,22])

# delete
# print(l.remove(33))
# print(l.pop())  # by default it remove the last element from the list
# print(l.clear())
# del l[2]
# del l[2:5]
# print(l)

# update
# var[index]=value
# var[start:end:step value] =iterable object

l = [90, 12, 33, 44, 55, 55, 66]
# l.count(55)
# print(l.count(55))

# l.reverse()

# l.sort()  # - mutable method is used to sort the list
# print(l)

# print(sorted(l))  # sorted is a immutable function takes iterable object

l.sort(reverse=True)  # - mutable method is used to sort the list
# print(l)

# print(sorted(l,reverse=False))  # sorted is a immutable function takes iterable object

# - all of these methods only posible on a list because list is mutable and ordered


# -------------
# set - set is a comma separated values within curly brasese {}
# syntax :
# var = {v1,v3,v3....} # variable name with values

# explain - set is unordered collection of unique elements , it will never maintain the sequence of it ,

# unordered -
# roll1 = {1, 2, 3, 4, 5, 6, "asdf", 7, 8, 9}
# print(roll1)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 'asdf'}

# mutable -
# roll = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# roll.add(70)
# print(roll)

# "set" is a heterogeneous collection of immutable elements/objects ,
# means all fundamental data types can be stored inside set

# heterogeneous collection -
# s1 = {23, 44, "hello", 2.3, True}
# print(s1)

# duplicate value is not allowed in set
# s2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(s2) # {1, 2, 3, 4, 5, 6, 7, 8, 9} - duplicate value is not allowed it will not print the duplicate value

# how to add data  -  add

x = ""  # string
x = []  # list
x = {}  # dictionary
x = ()  # tuple
x = set()  # set object empty

# set  - is a comma separated values within a curly bracess
# dictionary  - is a comma separated "key and value pair" within curly bracess

s = {1, 2, 3, 4}  # - set object
s = {2: 34, 45: 23, 23: 29}  # - dictionary object


# every object has a class

# class cls_name:
# operation performed related to the object
# by using methods

# obj2 = cls_name()  # -- to create object of class with a refrence name(obj2)

# example  -
#  class str:

# --

# example 1 .

t = ()
# print(type(t))

# t = set() # to define an empty set
# print(type(t))

s = {11, 22, 33}
s.clear()
# print(s)

# add
s = {22, 33, 44}
s.add(66)
# print(s)

# remove(),pop(),discard()

s = {22, 33, 44}
s.remove(33)
# print(s)

s1 = {22, 33, 44}
s = s1.pop() # it will return the deleted element 
# print(s1)
# print(s)

s = {22, 33, 44}
s.discard(22)  # if it not work it will not throw any error
# print(s)

sd= {23,45,56,6,77,454}

# print(sd.intersection(23)) 

# sd.difference([23,45])

# sd.symmetric_difference([23,45])

# print(sd)

b1 = {"kunal kale","rahul bhagat","rajesh patil","pavan kalyyan","pavan raut"}
b2 = {"kunal kale","rahul bhagat","rajesh patil","om jadhav","yogesh pandit"}
b3 = {"varun kale","ajay mirge","rahul bhagat","rajesh patil", "pavan kalyyan"}


# print(b1.intersection(b2,b3))  # it will give the common names from b1 and b2 and b3
# print(b1.difference(b2))  # it will give the names from b1 which is not present in b2
# print(b1.difference(b3,b2))  # it will give the names from b1 which is not present in b2,b3 - names form b1 which and not in b2 and b3
# print(b1.symmetric_difference(b2)) # it will give the names which are not present in both b1 and b2
# print(b1.symmetric_difference(b2,b3)) # it will give the names which are not present in both b1 and b2 and b3


# if "*" is given inside parrameter that means you can give more than one parameter in it 



# summary - 

s = {1,2,3,4,5}
# set is a unordered,mutable,heterogeneous collection of elements only , duplicate value is not allowed in it
# methods : add, remove, pop, discard, clear,intersection,difference,symmetric_difference