# Write a Python function using re.search() that checks if a string contains 
# a valid date in the format 'DD/MM/YYYY'. The function should return True 
# if a date is found, otherwise False.

import re

def has_valid_date(text):
    pattern = r'\b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}\b'
    match = re.search(pattern, text)
    return bool(match)

# Example usage:
text1 = "Your order was placed on 15/08/2026 successfully."
text2 = "Meeting scheduled for next Monday."

print("Contains valid date (Text 1):", has_valid_date(text1))
print("Contains valid date (Text 2):", has_valid_date(text2))
