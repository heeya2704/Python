# Given a dictionary called food_prices with 5 Zomato food items as keys and 
# their prices as values, write code to display all items that cost more than ₹200.

food_prices = {
    "Pizza": 350,
    "Burger": 180,
    "Biryani": 250,
    "Pasta": 220,
    "Sandwich": 150
}

print("Food items costing more than ₹200:")

for item, price in food_prices.items():
    if price > 200:
        print(item, "₹" + str(price))