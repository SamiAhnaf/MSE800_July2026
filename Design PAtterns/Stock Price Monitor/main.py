#Observer
class Observer:
    def update(self, peice):
        pass
#concrete observer
class Investor(Observer):
    def __init__(self, name):
        self.name = name
    def update(self, price):
        print(f"{self.name} received new stock price: {price}")
#subject
class Stock:
    def __init__(self):
        self.investors = []
        self.price = 0
    def subscribe(self, investor):
        self.investors.append(investor)
    def notify(self):
        for investor in self.investors:
            investor.update(self.price)
    def set_price(self, price):
        self.price = price
        self.notify()

#Create Investors
investor1 = Investor("Ali")
investor2 = Investor("Sara")
investor3 = Investor("John")
#Create Stock
stock = Stock()
#Subscribe Investors
stock.subscribe(investor1)
stock.subscribe(investor2)
stock.subscribe(investor3)
#Change Stock Price
stock.set_price(105)