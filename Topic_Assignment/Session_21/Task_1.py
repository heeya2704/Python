# Create a Python class called Product with attributes name and price, 
# and a method get_discounted_price() that returns the price after applying a 10% discount.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_discounted_price(self):
        return self.price * 0.90

# Example usage:
item = Product("T-Shirt", 1000.0)

print("Product Name:", item.name)
print("Original Price: Rs.", item.price)
print("Discounted Price (10% off): Rs.", item.get_discounted_price())
