"""Exercise: Payment System Using Polymorphism"""

class Payemnt:
    def pay(self):
        print("Starting Payment Process")


class CreditCard:
    def make_payment(self):
        print("Payment made using Credit Card")


class PayPal:
    def make_payment(self):
        print("Payment made using PayPal")


class BankTransfer:
    def make_payment(self):
        print("Payment made using Bank Transfer")

payment0 = Payemnt()
payment1 = CreditCard()
payment2 = PayPal()
payment3 = BankTransfer()

payment0.pay()
payment1.make_payment()
payment2.make_payment()
payment3.make_payment()