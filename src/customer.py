class Customer:
    def __init__(self, import_customer_name, import_customer_wallet, import_customer_age):
        self.customer_name = import_customer_name
        self.customer_wallet = import_customer_wallet
        self.customer_age = import_customer_age
    
    def buy_drink(self, drink):
        self.customer_wallet -= drink.price
