# Build a Product class for a Flipkart-style app with a private attribute _price. 
# Implement get_price() and set_price() methods to access and update the price. 
# Demonstrate setting and getting the price for a product object.

class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    def get_price(self):
        return self._price

    def set_price(self, new_price):
        if new_price >= 0:
            self._price = new_price
            print(f"Updated price for {self.name} to Rs. {new_price}")
        else:
            print("Error: Price cannot be negative.")

# Example usage:
product = Product("Wireless Headphones", 1999.0)

print("Product Name:", product.name)
print("Initial Price: Rs.", product.get_price())

product.set_price(1799.0)
print("Updated Price: Rs.", product.get_price())
