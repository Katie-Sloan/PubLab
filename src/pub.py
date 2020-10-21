class Pub:
    def __init__(self, import_name, import_till):
        self.name = import_name
        self.till = import_till
        self.inventory = []

    def add_inventory(self, drink):
        self.inventory.append(drink)
