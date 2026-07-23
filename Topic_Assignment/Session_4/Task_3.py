# Write a function split_product_code(product_code) that takes a string 
# like 'ZOMATO-FOOD-2024' and returns a list of its parts using the split() method.

def split_product_code(product_code):
    return product_code.split("-")

code = "ZOMATO-FOOD-2024"

print(split_product_code(code))