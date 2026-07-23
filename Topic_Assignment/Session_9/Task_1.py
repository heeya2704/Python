# Define a function called calculate_final_price(price, discount_rate) that 
# returns the final price after applying the discount rate to the given price.

def calculate_final_price(price, discount_rate):
    final_price = price - (price * discount_rate / 100)
    return final_price

# Example
print(calculate_final_price(1000, 20))