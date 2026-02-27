# day 4 of python

# format() method 👇

# "msg { } msg2 {} mag {}".format(
#     1, 2, 3
# )  # 1,2,3 will be replaced by {} & it can take anything(intiger , string, float,boolean,etc)

# for example

# num1 = 10
# num2 = 20
# sum = num1 + num2
# print(
#     "the sum of {} and {} is {}".format(num1, num2, sum)
# )  # this is how format method can be used in python for any data type

# print(
#     "the sum of {1} and {0} is {2}".format(num1, num2, sum)
# )  # you can change the index number to changer the position

# print(
#     "the sum of {fs} and {sd} is {um}".format(ft=num1, sn=num2, um=sum)
# )  # you can change key to change position of the formart

# -- f"" f-string method -- 👇

# print(
#     f"the sum of {num1} and {num2} is {sum}"
# )  # this is how f-string can be used in python and the most simple way of doint it

# name = "Adinath(Software developer)"
# city = "mumbai"

# print(f"i am {name} i live in {city}") # this string formatting is also called f-string

# h1 = "rol"
# h2 = "name"
# h3 = "course"
# h4 = "mumbai"
# print("-" * 85)
# print(
#     f"|{h1:^10}|{h2:^10}|{h3:^10}|{h4:^10}|"
# )  # here added width and alignment using f-string "10" is width and center-"^", right-">", left-"<"is alignment
# print("-" * 85)
 
name = 'kunal'
age=  "23"
city="mumbai"
print(f'name:{name}, age:{age}, city:{city}')  # this is using f-string method

# -- end