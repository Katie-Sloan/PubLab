class Pub:
    def __init__(self, import_name, import_till):
        self.name = import_name
        self.till = import_till
        self.inventory = []

    def add_inventory(self, drink):
        self.inventory.append(drink)

    def reduce_inventory(self):
        self.inventory -= 1

    def add_money_to_till(self, drink):
        self.till += drink.price

    def sell_drink(self, customer, drink):
        self.add_money_to_till(drink)
        customer.buy_drink(drink)
