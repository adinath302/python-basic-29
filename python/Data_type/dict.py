# dict(dictonary) in python

# topic - Data type
# dict
# - methods
# explain -

# revision  -
# all fundamental data types are immutable and tuple and frozenset are immutable
# immutale data type - str,int,float,complex,bool,tuple,frozenset

# dict -
# mutable , comma sep key and value pairs within {}, it can keep duplicate values

# key - should be immutable only (string,integer,tuple,frozenset), it should be unique (not duplicate)

# values - any data type can be used(mutable or immutable), accepts duplicate

# syntax :
#  var ={k1=v1,k2:v2,k3:v3...}

# example
s1 = {"name": "raj", "age": 23, "persentage": 78.99}
# print(type(s1))  # <class 'dict'>

# example 2
s2 = {
    "hindi": 78.56,
    "english": 78.90,
    "maths": 45.76,
}  # here the subject is key and the persentage is value

# example 3
marks = {"kale": 67, "ak": 67, "jh": 79}  # key is string(immutable)

# example 4
chapter1 = {
    1.1: "introductin",
    1.2: "class and object",
    1.3: "attribute and methods",
}  # key is float(immutable)

# example 5
square = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}  # key is integer(immutable)

# example 6

s = {
    1: 23,
    2: 44,
    3: 67,
    2: 21,
}  # when you use duplicate key then it will overwrite the the previous value (key should be unique)
print(s)  # {1: 23, 2: 21, 3: 67}
print(type(s))  # <class 'dict'>

# example 7

details = {
    "name": "keshav",
    "age": 21,
    "per": 89.55,
    "lang": ["python", "javascript", "typescript", "c++"],
    "marks": {
        "python": 99.9,
        "javascript": 99.9,
        "typescript": 99.9,
        "c++": 99.9,
    },
}  # you can store any data type in dict(immutable and mutable)

# example 8

x = {
    "andhra pradesh": "amaravati",
    "maharashtra": "mumbai",
    "uttar pradesh": "lucknow",
    "haryana": "chandigarh",
    "rajasthan": "jaipur",
}

# example 8

sk = {
    "pune": ["haveli", "chinchwad", "junnar", "ambegoan"],
    "nashik": ["surgana", "malegoan", "nandgaon"],
    "nagpur": ["kamptee", "hingna", "katol", "savner"],
}

# example 9

dd = {
    "python": "Guido van Rossum",
    "java": "James Gosling",
    "javascript": "Brendan Eich",
    "C++": "Bjarne Stroustrup",
    "c": "Dennis Ritchie",
}

# example 10

s2 ={'name':"ketan",'age':78} # single students

1311 = {1:{"name":"rahul","age":22},2:{'name':'vaib','age':23},3:{"name":"keshav","age":89},4:{"name":"kartik","age":11}} # batch of students(nested dict)

python = {
    "batch-1311":{1:{"name":"parik","age":67},2:{"name":'kirti','age':98},3:{"name":'patil','age':56}},
    "batch-1312" :{1:{"name":"pooja","age":67},2:{"name":'kirti','age':98},3:{"name":'patil','age':56}},
    "batch-1313":{1:{"name":"kartik","age":56},2:{"name":"sada",'age':89},3:{"name":"shyam","age":45}},
    } # nested dict
          
# example 11 -

sd = {"faculty":{"employee1":{"name":"keshav","company":"adb"},"employee2":{"name":"parth","company":"asd"}}}

# 26