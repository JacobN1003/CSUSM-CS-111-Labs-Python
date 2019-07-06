#Receipt
#Jacob Norenberg
#July 3, 2019

item1 = input("Enter item 1: ")
price1 = input("What's the price of " + item1 + "?: ")
item2 = input("Enter item 2: ")
price2 = input("What's the price of " + item2 + "?: ")
item3 = input("Enter item 3: ")
price3 = input("What's the price of " + item3 + "?: ")
subtotal = float(price1)+float(price2)+float(price3)
tax = float(subtotal) * 0.0725
total = float(tax) + float(subtotal)
print("*************************")
print(item1.ljust(23-len(price1)) + "$ " + price1)
print(item2.ljust(23-len(price2)) + "$ " + price2)
print(item3.ljust(23-len(price3)) + "$ " + price3)
print("\nSubtotal".ljust(24-len(str(subtotal))) + "$", round(float(subtotal),2))
print("Tax".ljust(23-len(str(tax))) + "$", round(float(tax),2))
print("Total".ljust(23-len(str(total))) + "$", round(float(total),2))
print("*************************")
print(" Thank you for Shopping!")
print("*************************")
