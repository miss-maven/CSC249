# CSC 249 M2T2 python 
# Jane Martin
# 2/10/23

# THis is the widget store program that will show how many are in stock and the cost. 

widget_name = "widget"
widget_price = 1.90
widget_stock = 100

#greetings get name
print("Welcome to the widget store!")

cust_name = input("What is your name? ")

#advertize 
print("Hello, " + cust_name + "!")
print("We currently have " + str(widget_stock) + " " + widget_name + " in stock.")

widget_buy_Quant = int(input("How many " + widget_name + " do you want to purchase? "))

#show user gross price
gross_price = widget_price * widget_buy_Quant
print("The total cost of your order is: $" + str(gross_price))
print("THank you have a great day! ")