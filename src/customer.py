class Customer:
    def __init__(self, import_customer_name, import_customer_wallet, import_customer_age):
        self.name = import_customer_name
        self.wallet = import_customer_wallet
        self.age = import_customer_age
    
    def buy_drink(self, drink):
        self.wallet -= drink.price
