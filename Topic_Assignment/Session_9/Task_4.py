# Build a function called apply_coupon(price, coupon_code=None) that 
# returns the price after a 10% discount if coupon_code is 'ZOMATO10', 
# otherwise returns the original price.<br><br><em><strong>Constraint:</strong> 
# Use a default argument for coupon_code.</em>

def apply_coupon(price, coupon_code=None):
    if coupon_code == 'ZOMATO10':
        return price - (price * 10 / 100)
    else:
        return price    
    
# Example
print(apply_coupon(1000, 'ZOMATO10'))  # return 900.0
print(apply_coupon(1000))  # return 1000.0