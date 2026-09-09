# Create a class called FoodOrder with attributes: restaurant_name, items (list), 
# and total_price. Write an __init__() constructor to initialize these, 
# then create an object representing your last Zomato or Swiggy order and print its details.

class FoodOrder:
    def __init__(self, restaurant_name, items, total_price):
        self.restaurant_name = restaurant_name
        self.items = items
        self.total_price = total_price

# Example usage:
my_order = FoodOrder("La Pino'z Pizza", ["Paneer Tikka Pizza", "Garlic Bread"], 450.0)

print("Food Order Details:")
print("Restaurant Name:", my_order.restaurant_name)
print("Items:", my_order.items)
print("Total Price: Rs.", my_order.total_price)
