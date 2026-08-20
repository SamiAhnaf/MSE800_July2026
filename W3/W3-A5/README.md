**MONEY EXCHANGE RECORD DATABASE**

**TABLE DESCRIPTION:**

1. Customer

The Customer table stores information about customers who use the money exchange service. It contains details such as the customer's name, email, phone number, and address.

Using this the system will be able to keep track of who is making each currency exchange transaction.

2. Currency

The Currency table stores the currencies supported by the money exchange business. It contains the currency code, currency name, and symbol, such as NZD, USD, AUD, GBP, and EUR.

Now, the system can manage different currencies without repeatedly storing the same currency information.

3. Exchange_Rate

The Exchange_Rate table stores the exchange rates between two currencies. It records the source currency, target currency, exchange rate, and the date of the rate.

The system needs to know how much one currency is worth compared to another currency when calculating an exchange.

4. Exchange_Transaction

The Exchange_Transaction table stores the actual currency exchanges made by customers. It records the customer, exchange rate, amount, converted amount, transaction date, and transaction type.

This table keeps a record of every currency exchange made by a customer.