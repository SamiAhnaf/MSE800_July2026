class BankAccount:
    def __init__(self, account_number, customer_name, balance): #bank account needs account number, customer name, and balance
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    def display_details(self): #allowing the user to view their account details
        print(f"Account Number: {self.account_number}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Balance: ${self.balance}")

    def deposit(self, amount): #allowing user to deposit money into their account
        self.balance += amount
        print(f"${amount} deposited successfully.")

    def  withdraw(self, amount): #allowing user to withdraw money from their account
        if amount <= self.balance:
            self.balance -= amount
            print(f"${amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

class SavingsAccount(BankAccount):

    def calculate_interest(self, interest_rate):
        interest = self.balance * interest_rate / 100
        print(f"Interest earned: ${interest}")

    def account_type(self):
        print("Account Type: Savings Account")

# Create a Savings Account object
sami_account = SavingsAccount("SA1001", "Sami", 5000)

# Demonstrate all operations
sami_account.account_type()
sami_account.display_details()

sami_account.deposit(1000)
sami_account.withdraw(500)

sami_account.display_details()
sami_account.calculate_interest(5)
