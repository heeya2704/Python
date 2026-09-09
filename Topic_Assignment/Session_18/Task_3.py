# Given a block of text containing multiple prices (like 'Rs. 299', 'Rs. 1500', etc.), 
# use re.findall() to extract all the numeric price values as integers and print their sum.
# Hint: Look for patterns like 'Rs. ' followed by one or more digits.

import re

text = "Item 1 costs Rs. 299, Item 2 costs Rs. 1500, and delivery is Rs. 50."

price_strings = re.findall(r'Rs\.\s*(\d+)', text)
prices = [int(price) for price in price_strings]

total_sum = sum(prices)

print("Extracted Prices:", prices)
print("Total Sum of Prices: Rs.", total_sum)
