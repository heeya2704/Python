# Use re.findall() to extract all valid phone numbers from a given string 
# in the format '+91-XXXXXXXXXX' (e.g., '+91-9876543210'). Print the list of found numbers.

import re

text = "Contact support at +91-9876543210 or +91-9123456789. Alternate number: +91-8888877777."

phone_numbers = re.findall(r'\+91-\d{10}', text)

print("Extracted Phone Numbers:")
print(phone_numbers)
