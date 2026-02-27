# day 8 of python challenge -
# topic to cover --

# Taks -

# Task 1 - movie ticket billing system

# customer_name = input("Enter customer name - ")
# num_of_tickets = int(input("enter number of tickets - "))
# ticket_price = 250

# Total_bill = num_of_tickets * ticket_price
# print(
#     f"hello {customer_name}, your total bill for {num_of_tickets} tickets is Rs- {Total_bill}"
# )

# example 2
# name = input("Enter your name - ")
# ticket = int(input("enter your ticket -"))
# price = 250

# total = ticket * price
# print(f"Customer Name - {name} \n, your total bill for {ticket} tickets is rs - {total}") # fstring

# task 2 - salary slip generation

# Employee_name = input("enter employee name - ")
# salrary = int(input("enter your salary - "))
# hra = (20 / 100) * salrary
# da = (10 / 100) * salrary
# gs = salrary + hra + da
# tax = gs * 10/100
# net_salary = gs - tax

# print(
#     f"employee name -{Employee_name},\n salary - {salrary},\n hra -{hra},\n da - {da},\n gross salary - {gs},\n tax - {tax},\n net salary - {net_salary} "
# )

# Task 3
# Area & cost of painting

# owner_name = input("enter owner name - ")
# length_of_wall = eval(input("enter length of wall -"))
# breadth_of_wall = eval(input("enter breadth of wall -"))
# painting_cost_per_sq = 15

# Area_of_wall = length_of_wall * breadth_of_wall
# total_cost = Area_of_wall * painting_cost_per_sq

# print(f"Owner name - {owner_name},\n Area of wall - {Area_of_wall},\n Total cost - {total_cost}")

# timeframe is 1:04:34

# task 4 - mobail recharge bill

# customer_name = input("enter customer name - ")
# recharge_amount = int(input("enter recharge amount - "))

# gst = (18 / 100) * recharge_amount
# final_bill = recharge_amount + gst

# print(f"customer name - {customer_name}, \n recharge amount - {recharge_amount},\n GST - {gst},\n final bill - {final_bill}")

# task 5 - online food order bill

c_name = input("enter customer name - ")
itme_price = int(input("food item price - "))

delivery_charge = 40

gst = itme_price * 5 / 100
total_bill = itme_price + gst + delivery_charge

print(
    f"customer name - {c_name},\n item price - {itme_price}, \n GST - {gst}, \n delivery charge - {delivery_charge}, \n total bill - {total_bill}"
)

# end of day 8