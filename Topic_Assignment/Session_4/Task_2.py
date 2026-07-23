# Given the product name ' OnePlus Nord-CE 3 ', write code to clean it 
# by removing extra spaces, converting all letters to uppercase, and 
# replacing the dash with a colon.<br><br><em><strong>Hint:</strong>
# Use strip(), upper(), and replace() methods in sequence.</em>

product = " OnePlus Nord-CE 3 "

clean_product = product.strip().upper().replace("-", ":")

print(clean_product)