# Write a function show_final_price(item) that takes any Product or Electronics 
# object and prints its name and the discounted price by calling get_discounted_price(). 
# Demonstrate polymorphism by passing both a Product and an Electronics object to this function.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_discounted_price(self):
        return self.price * 0.90

class Electronics(Product):
    def get_discounted_price(self):
        return self.price * 0.80

def show_final_price(item):
    final_price = item.get_discounted_price()
    print(f"Item: {item.name} | Original: Rs. {item.price} | Final Discounted Price: Rs. {final_price}")

# Example usage:
standard_item = Product("Backpack", 2000.0)
tech_item = Electronics("Laptop", 50000.0)

print("Demonstrating Polymorphism:")
show_final_price(standard_item)
show_final_price(tech_item)
