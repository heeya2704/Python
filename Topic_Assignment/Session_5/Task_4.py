# Create a tuple called insta_filters with 4 Instagram filter names (as strings). 
# Try to change the first filter name and observe what error you get.
# <br><br><em><strong>Hint:</strong> Tuples are immutable.
# Note down the error message.</em>

insta_filters = ("Clarendon", "Gingham", "Juno", "Lark")

# Trying to modify the first element
insta_filters[0] = "Valencia"

# It will raise a TypeError: 'tuple' object does not support item assignment, 
# because tuples are immutable and cannot be changed after creation.