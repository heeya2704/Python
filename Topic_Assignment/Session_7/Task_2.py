# Create a Python program that asks the user to enter their Zomato order amount and 
# checks if it is above 300; if yes, print 'Eligible for free delivery', 
# else print 'Delivery charges apply'.

order_amount = float(input("Enter your Zomato order amount: "))

if order_amount > 300:
    print("Eligible for free delivery")
else:
    print("Delivery charges apply")