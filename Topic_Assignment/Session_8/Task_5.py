# Build a simple shopping cart total calculator: Given a list of item prices 
# from a Flipkart cart, use a loop to sum the prices. If an item price is 0 (out of stock), 
# skip it. Stop adding items if the running total crosses ₹2000 using break, and 
# print the final total.<br><br><em><strong>Constraint:</strong> Use both break and 
# continue in your solution.</em>

cart_prices = [450, 800, 0, 650, 300, 900, 250]

total = 0

for price in cart_prices:
    if price == 0:
        continue

    total += price

    if total > 2000:
        break

print("Final Total: ₹", total)