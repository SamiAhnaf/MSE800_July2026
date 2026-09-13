"""Exercise: ATM System Using Abstraction"""

from abc import ABC, abstractmethod

class ATM(ABC):
    @abstractmethod
    def insert_card(self):
        pass

    @abstractmethod
    def enter_pin(self):
        pass

    @abstractmethod
    def check_balance(self):
        pass

    @abstractmethod
    def withdraw_cash(self, amount):
        pass

class MyATM(ATM):
    def __init__(self, balance):
        self.balance = balance

    def insert_card(self):
        print("Card inserted successfully.")

    def enter_pin(self):
        print("PIN entered successfully.")

    def check_balance(self):
        print(f"Current Balance: ${self.balance}")

    def withdraw_cash(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"${amount} withdrawn successfully.")
            print(f"Remaining Balance: ${self.balance}")
        else:
            print("Insufficient balance.")


atm1 = MyATM(1000)

atm1.insert_card()
atm1.enter_pin()
atm1.check_balance()
atm1.withdraw_cash(200)