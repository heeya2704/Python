# Create a function called get_delivery_charge(amount, city='Ahmedabad') that 
# returns 0 if city is 'Ahmedabad', otherwise returns 50 as a delivery charge.
# <br><br><em><strong>Hint:</strong> Use a default argument for the city parameter.</em>

def get_delivery_charge(amount, city="Ahmedabad"):
    if city == "Ahmedabad":
        return 0
    else:
        return 50

# Examples
print(get_delivery_charge(500))
print(get_delivery_charge(500, "Surat"))