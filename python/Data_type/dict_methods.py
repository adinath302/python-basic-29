# dict methods -
# dict
# methods
# - CRUD(create , read , update , delete) OPERATIONS

# when you hover on a method -
# "*" if only one star is present inside parameter it means you can give multiple comma separated value in it
# "**" but if the 2 star then you have to give the value like  - parameter = value then python convert it into key and value pairs

# revision -
# dict is a mutable data type with comma separated key and value pairs within {}
# var = {"name": "ketan", "age": 23, "persentage": 78.99}

# key - unique and immutable
# values - any type of values can be used(mutable and immutable) and accepts duplicate values

# dict methods -
# crud operations -

# create -
emp = {
    "name": "pratik",
    "skills": ["web development", "data science", "machine learning"],
    "salary": 50000,
}

dev = {
    "id321": {"name": "ketan", "salary": 50000},
    "id322": {"name": "kusha", "salary": 60000},
}

# read -

# how to access data from dict

# 1. syntax -
# var[key]- variable name and key - if the key is not found it will throw an error

# dev["name"]
# print(dev["id321"]["name"])

data = {"name": "ketan", "age": 25, "salary": 2399, "city": "pune"}

# print(data["city"])

# get method - even if the key is not found it will not throw any error

# 2. syntax  - var.get(key) - variable name .get and key
# example  -
x = {"name": "heki", "age": 25, "salary": 2399, "city": "nagpur"}

# print(x.get("name"))
# print(
# x.get("marks", "not found")
# )  # not found is the default value if the key is not found but it will not throw any error


# add - we can add single value to the dict
# syntax -
x = {"name": "kiran"}
# 1. var[key]=value  - variable name and key and value you want to add to the dict
# example -
x["age"] = 45

x["city"] = "mumbai"

# print(x)


# update -
# by using 'update' we can add multiple values
# syntax -
# example 1. -

w = {"name": "sdds"}
w.update(city="mumbai", marks=299)
# print(w)

# example 2.  -
s1 = {1: 1, 2: 2, 3: 3}
s2 = {4: 4, 5: 5, 6: 6}
s1.update(s2)
# print(s1)

# example 3. -
b1 = {1: {"name": "ketan", "age": 34}, 2: {"name": "kusha", "age": 23}}

# add - variable name - key and it's vlue

b1[1]["city"] = "mumbai"
b1[2]["city"] = "pune"
# print(b1[1])

# access -

# print(b1[1])
# print(b1[1]['age'])
# print(b1[2]['age'])
# print(b1[2]['name'])


# get -
b2 = {1: {"name": "ketan", "age": 34}, 2: {"name": "kusha", "age": 23}}

# print(b2.get(1))
# print(b2[1].get("name"))
# print(b2[2].get("name"))

# update -

b2[1].update(percentage=23)  #
# print(b2[1])

b3 = {}

b3["name"] = "ketan"
# print(b3["name"])
# print(b3)

# example -
product = {"name": "fan", "id": 1023, "price": 3000}

# print(product["price"])
sd = product["price"]

product["city"] = "pune"
# print(product)

# example -
iphone = {
    "iphone11": {"price": 58000, "color": "black"},
    "iphone12": {"price": 90000},
    "iphone14": {"price": 120000, "color": "red", "ram": "8gb"},
}

# print(iphone["iphone12"].get("price"))
# print(iphone["iphone14"]["ram"])
# print(iphone["iphone11"]['color'])
# iphone["iphone12"]["storage"] = "128gb"
# print(iphone["iphone12"])

# example  -

mm = iphone["iphone11"]["price"]  # 58000
bb = (mm * 10) / 100  # 5800
sp = mm - bb  # 52000

iphone["iphone11"]["selling_price"] = int(sp)
# print(iphone["iphone11"])  # 52000

iphone["iphone14"]["ram"] = "16gb"  # you can change the value
# print(iphone["iphone14"])

vivo_19 = {"ram": "8gb", "color": "white", "price": 20000}

# sj = vivo_19.pop("color")  # the pop will return the deleted value in the "sj"
# print(sj)

# print(vivo_19.popitem())  # in return it will you the deleted key and value pair only
# print(vivo_19)

# CRUD OPERATION -

# x1 = {"name": "ketan", "age": 23, "city": "pune", "country": "india"}

# x1["phone"] = (7822901803)  # Create 3   {'name': 'ketan', 'age': 23, 'city': 'pune', 'country': 'india', 'phone': 7822901803})
# print(x1["phone"])  # Read - 1   # 7822901803
# print(x1.get("phone"))  # Read - 2   # 7822901803
# x1.update(pincode=42388)  # Update   {'name': 'ketan', 'age': 23, 'city': 'pune', 'country': 'india', 'phone': 7822901803, 'pincode': 42388}
# x1.pop("name")  # Delete   {'age': 23, 'city': 'pune', 'country': 'india', 'phone': 7822901803}
# print(x1)


x1 = {"name": "ketan", "age": 23, "city": "pune", "country": "india"}
# print(x1.keys())  # dict_keys(['name', 'age', 'city', 'country']) list of keys in dict

# print(x1.values()) # dict_values(['ketan', 23, 'pune', 'india']) list of values in dict

# print(
# x1.items()
# )  # dict_items([('name', 'ketan'), ('age', 23), ('city', 'pune'), ('country', 'india')]) list of key and value pairs - list of tuples of key and value

# print(x1.clear()) # it will clear the dict

# 1. It is the most efficient way to create a new dictionary where multiple keys need to start with the same initial value (like 0, False, or None).

#  example  categories = ['electronics', 'clothing', 'home']
# inventory = dict.fromkeys(categories, 0)
# Result: {'electronics': 0, 'clothing': 0, 'home': 0}

xx = x1.fromkeys(
    x1, "ketan"
)  # {'name': 'ketan', 'age': 'ketan', 'city': 'ketan', 'country': 'ketan'}
xx1 = x1.fromkeys()
# print(xx)

# 2. Because dictionary keys must be unique, fromkeys() can quickly remove duplicates from a list while preserving the original order of the elements. 

# numbers = [1, 2, 2, 3, 4, 4, 5]
# unique_numbers = list(dict.fromkeys(numbers))
# Result: [1, 2, 3, 4, 5]
