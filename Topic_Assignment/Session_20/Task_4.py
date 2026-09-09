# Design a simple abstract class PaymentMethod with an abstract method pay(amount). 
# Then, create two subclasses: Paytm and PhonePe, each implementing pay(amount) 
# to print a different message. Instantiate both and call their pay methods with any amount.

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class Paytm(PaymentMethod):
    def pay(self, amount):
        print(f"Paid Rs. {amount} successfully using Paytm UPI.")

class PhonePe(PaymentMethod):
    def pay(self, amount):
        print(f"Paid Rs. {amount} successfully using PhonePe UPI.")

# Example usage:
paytm_payment = Paytm()
phonepe_payment = PhonePe()

paytm_payment.pay(250.0)
phonepe_payment.pay(500.0)
