# Create a Paytm cashback calculator that asks for total spend and 
# number of offers applied, then divides spend by offers to show average 
# cashback per offer. If the number of offers is zero, raise a custom exception 
# called NoOffersApplied and display a custom error message.<br><br><em><strong>
# Hint:</strong> Define your own exception class by subclassing Exception.</em>

class NoOffersApplied(Exception):
    pass

try:
    total_spend = float(input("Enter total spend: "))
    offers = int(input("Enter number of offers applied: "))

    if offers == 0:
        raise NoOffersApplied("No offers applied. Cashback cannot be calculated.")

    average_cashback = total_spend / offers

    print("Average Cashback per Offer:", average_cashback)

except NoOffersApplied as e:
    print(e)