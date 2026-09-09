# Extend the FoodOrder class by adding a method add_item(self, item_name, item_price) 
# that adds the item to the items list and updates total_price. Demonstrate by adding 
# two items to your order and printing the updated total.

class FoodOrder:
    def __init__(self, restaurant_name, items, total_price):
        self.restaurant_name = restaurant_name
        self.items = items
        self.total_price = total_price

    def add_item(self, item_name, item_price):
        self.items.append(item_name)
        self.total_price += item_price
        print(f"Added '{item_name}' (Rs. {item_price}) to the order.")

# Example usage:
my_order = FoodOrder("McDonald's", ["McVeggie Burger"], 120.0)

print("Initial Order:")
print("Items:", my_order.items)
print("Total Price: Rs.", my_order.total_price)

print("\nAdding items:")
my_order.add_item("Fries", 80.0)
my_order.add_item("Coke", 60.0)

print("\nUpdated Order:")
print("Items:", my_order.items)
print("Updated Total Price: Rs.", my_order.total_price)
