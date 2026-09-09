# Create a generator function called order_id_generator that yields a new 
# order ID (starting from 1001) each time it's called, similar to how Zomato or 
# Swiggy generates unique order numbers.
# Hint: Use the yield statement inside a loop to generate the next ID.

def order_id_generator(start_id=1001):
    current_id = start_id
    while True:
        yield current_id
        current_id += 1

# Example usage:
order_gen = order_id_generator()

print("Generated Order IDs:")
print("Order 1 ID:", next(order_gen))
print("Order 2 ID:", next(order_gen))
print("Order 3 ID:", next(order_gen))
print("Order 4 ID:", next(order_gen))
