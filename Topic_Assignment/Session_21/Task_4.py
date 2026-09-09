# Build a simple Ticket class for a movie booking app with a method get_final_price(). 
# Then, create a subclass PremiumTicket that overrides get_final_price() to add a 50 rupee 
# convenience fee. Show both in action by creating objects and printing their final prices.
# Hint: Use super() in PremiumTicket to reuse the parent method and add the extra fee.

class Ticket:
    def __init__(self, movie_name, price):
        self.movie_name = movie_name
        self.price = price

    def get_final_price(self):
        return self.price

class PremiumTicket(Ticket):
    def get_final_price(self):
        base_price = super().get_final_price()
        convenience_fee = 50.0
        return base_price + convenience_fee

# Example usage:
standard_ticket = Ticket("Avatar: The Way of Water", 250.0)
premium_ticket = PremiumTicket("Avatar: The Way of Water (IMAX 3D)", 450.0)

print(f"Standard Ticket ({standard_ticket.movie_name}): Rs. {standard_ticket.get_final_price()}")
print(f"Premium Ticket ({premium_ticket.movie_name}): Rs. {premium_ticket.get_final_price()} (Includes Rs. 50 convenience fee)")
