#target YALLAHABIBI
class Payment:
    def pay(self, amount):
        pass
#Adaptee
class OldPaymentSystem:
    def make_payment(self, amount):
        print(f"Payment of ${amount} made using Old Payment System.")
#Adapter
class PaymentAdapter(Payment):
    def __init__(self, old_payment):
        self.old_payment = old_payment
    def pay(self, amount):
        self.old_payment.make_payment(amount)
#client
old_payment = OldPaymentSystem()
adapter = PaymentAdapter(old_payment)
adapter.pay(500)