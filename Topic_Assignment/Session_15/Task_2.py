# Build a Flipkart-style price-per-item calculator: take total cart amount and 
# item count as input, perform division, and use try-except to catch and display 
# a user-friendly message if the item count is zero.

def calculate_price_per_item(total_cart_amount, item_count):
    try:
        if item_count == 0:
            raise ValueError("Item count cannot be zero.")
        return total_cart_amount / item_count

    except ValueError as e:
        print(f"Error: {e}")
        return None

# Example usage:
total_cart_amount = float(input("Enter total cart amount: "))
item_count = int(input("Enter item count: "))
price_per_item = calculate_price_per_item(total_cart_amount, item_count)