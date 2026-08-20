import sqlite3


class MoneyExchangeDatabase:
    def __init__(self, database_name="money_exchange.db"):
        self.database_name = database_name
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

        # Enable foreign key constraints
        self.cursor.execute("PRAGMA foreign_keys = ON")
 
    # CREATE DATABASE TABLES

    def create_tables(self):

        # Customer table
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Customer (
            customer_id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT,
            phone TEXT,
            address TEXT
        )
        """)

        # Currency table
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Currency (
            currency_id INTEGER PRIMARY KEY,
            currency_code TEXT UNIQUE NOT NULL,
            currency_name TEXT NOT NULL,
            symbol TEXT
        )
        """)

        # Exchange Rate table
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Exchange_Rate (
            rate_id INTEGER PRIMARY KEY,
            from_currency_id INTEGER NOT NULL,
            to_currency_id INTEGER NOT NULL,
            exchange_rate REAL NOT NULL,
            rate_date TEXT NOT NULL,

            FOREIGN KEY (from_currency_id)
                REFERENCES Currency(currency_id),

            FOREIGN KEY (to_currency_id)
                REFERENCES Currency(currency_id)
        )
        """)

        # Exchange Transaction table
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Exchange_Transaction (
            transaction_id INTEGER PRIMARY KEY,
            customer_id INTEGER NOT NULL,
            rate_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            converted_amount REAL NOT NULL,
            transaction_date TEXT NOT NULL,
            transaction_type TEXT NOT NULL,

            FOREIGN KEY (customer_id)
                REFERENCES Customer(customer_id),

            FOREIGN KEY (rate_id)
                REFERENCES Exchange_Rate(rate_id)
        )
        """)

        self.connection.commit()

        print("Tables created successfully.")

    # INSERT CUSTOMERS    

    def insert_customers(self):

        customers = [
            (1, "Sami", "Ahnaf",
             "sami@example.com", "0211111111", "Auckland"),

            (2, "Bleh", "Rahman",
             "bleh@example.com", "0212222222", "Auckland"),

            (3, "Dark", "Bright",
             "dark@example.com", "0213333333", "Hamilton"),

            (4, "Who", "Who",
             "who@example.com", "0214444444", "Wellington"),

            (5, "Gg", "Wilson",
             "gg@example.com", "0215555555", "Christchurch")
        ]

        self.cursor.executemany("""
        INSERT OR IGNORE INTO Customer
        (customer_id, first_name, last_name, email, phone, address)
        VALUES (?, ?, ?, ?, ?, ?)
        """, customers)

        self.connection.commit()

        print("Customers inserted successfully.")

    # INSERT CURRENCIES   

    def insert_currencies(self):

        currencies = [
            (1, "NZD", "New Zealand Dollar", "$"),
            (2, "USD", "United States Dollar", "$"),
            (3, "AUD", "Australian Dollar", "$"),
            (4, "GBP", "British Pound", "£"),
            (5, "EUR", "Euro", "€")
        ]

        self.cursor.executemany("""
        INSERT OR IGNORE INTO Currency
        (currency_id, currency_code, currency_name, symbol)
        VALUES (?, ?, ?, ?)
        """, currencies)

        self.connection.commit()

        print("Currencies inserted successfully.")
   
    # INSERT EXCHANGE RATES

    def insert_exchange_rates(self):

        exchange_rates = [
            # rate_id, from_currency, to_currency, rate, date

            (1, 1, 2, 0.59, "2026-08-20"),   # NZD -> USD
            (2, 2, 1, 1.69, "2026-08-20"),   # USD -> NZD

            (3, 1, 3, 0.91, "2026-08-20"),   # NZD -> AUD
            (4, 3, 1, 1.10, "2026-08-20"),   # AUD -> NZD

            (5, 1, 4, 0.45, "2026-08-20"),   # NZD -> GBP
            (6, 4, 1, 2.22, "2026-08-20"),   # GBP -> NZD

            (7, 1, 5, 0.54, "2026-08-20"),   # NZD -> EUR
            (8, 5, 1, 1.85, "2026-08-20")    # EUR -> NZD
        ]

        self.cursor.executemany("""
        INSERT OR IGNORE INTO Exchange_Rate
        (rate_id, from_currency_id, to_currency_id,
         exchange_rate, rate_date)
        VALUES (?, ?, ?, ?, ?)
        """, exchange_rates)

        self.connection.commit()

        print("Exchange rates inserted successfully.")

    # INSERT TRANSACTIONS   

    def insert_transactions(self):

        transactions = [
            # ID, customer, rate, amount,
            # converted amount, date, type

            (1, 1, 1, 1000.00, 590.00,
             "2026-08-20 10:00", "Buy"),

            (2, 2, 2, 500.00, 845.00,
             "2026-08-20 10:30", "Sell"),

            (3, 3, 3, 800.00, 728.00,
             "2026-08-20 11:00", "Buy"),

            (4, 4, 5, 1000.00, 450.00,
             "2026-08-20 11:30", "Buy"),

            (5, 5, 7, 600.00, 324.00,
             "2026-08-20 12:00", "Sell")
        ]

        self.cursor.executemany("""
        INSERT OR IGNORE INTO Exchange_Transaction
        (transaction_id, customer_id, rate_id,
         amount, converted_amount,
         transaction_date, transaction_type)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, transactions)

        self.connection.commit()

        print("Transactions inserted successfully.")

    # DISPLAY CUSTOMERS
     
    def show_customers(self):

        print("\n--- CUSTOMERS ---")

        self.cursor.execute("""
        SELECT customer_id, first_name, last_name, email
        FROM Customer
        """)

        customers = self.cursor.fetchall()

        for customer in customers:
            print(customer)
     
    # DISPLAY CURRENCIES

    def show_currencies(self):

        print("\n--- CURRENCIES ---")

        self.cursor.execute("""
        SELECT currency_code, currency_name, symbol
        FROM Currency
        """)

        currencies = self.cursor.fetchall()

        for currency in currencies:
            print(currency)

    # DISPLAY TRANSACTIONS
     
    def show_transactions(self):

        print("\n--- EXCHANGE TRANSACTIONS ---")

        query = """
        SELECT
            Exchange_Transaction.transaction_id,
            Customer.first_name || ' ' || Customer.last_name
                AS customer_name,
            Currency.currency_code AS from_currency,
            Currency2.currency_code AS to_currency,
            Exchange_Transaction.amount,
            Exchange_Transaction.converted_amount,
            Exchange_Transaction.transaction_type,
            Exchange_Transaction.transaction_date

        FROM Exchange_Transaction

        JOIN Customer
            ON Exchange_Transaction.customer_id =
               Customer.customer_id

        JOIN Exchange_Rate
            ON Exchange_Transaction.rate_id =
               Exchange_Rate.rate_id

        JOIN Currency
            ON Exchange_Rate.from_currency_id =
               Currency.currency_id

        JOIN Currency AS Currency2
            ON Exchange_Rate.to_currency_id =
               Currency2.currency_id
        """

        self.cursor.execute(query)

        transactions = self.cursor.fetchall()

        for transaction in transactions:
            print(transaction)

    # CLOSE DATABASE

    def close_database(self):

        self.connection.close()

        print("\nDatabase connection closed.")

# MAIN PROGRAM

def main():

    # Create database object
    database = MoneyExchangeDatabase()

    # Create tables
    database.create_tables()

    # Insert sample data
    database.insert_customers()
    database.insert_currencies()
    database.insert_exchange_rates()
    database.insert_transactions()

    # Display data
    database.show_customers()
    database.show_currencies()
    database.show_transactions()

    # Close database
    database.close_database()


# Run the program
if __name__ == "__main__":
    main()