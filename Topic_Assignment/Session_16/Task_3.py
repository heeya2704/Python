# Use enumerate() to print out the index and name of each item in a 
# shopping cart list (e.g., ['Pizza', 'Burger', 'Fries', 'Coke']) 
# like Flipkart displays item numbers in your cart.

cart_items = ['Pizza', 'Burger', 'Fries', 'Coke']

print("Flipkart Shopping Cart:")
for index, item in enumerate(cart_items, start=1):
    print(f"Item {index}: {item}")
