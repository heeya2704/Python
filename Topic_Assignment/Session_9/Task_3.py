# Write a function called format_price(price, currency='INR') that 
# returns a string like '₹500' if currency is 'INR', or '$500' if currency is 'USD'.

def format_price(price, currency="INR"):
    if currency == "INR":
        return f"₹{price}"
    elif currency == "USD":
        return f"${price}"

# Examples
print(format_price(500))
print(format_price(500, "USD"))