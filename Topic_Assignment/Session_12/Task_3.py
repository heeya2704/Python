# Use reduce() from functools to calculate the total price of items in a 
# Flipkart shopping cart: [499, 1299, 299, 799]. Print the final total.
# <br><br><em><strong>Hint:</strong> Import reduce from functools and 
# use a lambda to sum two numbers.</em>

from functools import reduce

cart = [499, 1299, 299, 799]

total = reduce(lambda x, y: x + y, cart)

print("Total Price:", total)