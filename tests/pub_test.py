import unittest
from src.pub import Pub
from src.drinks import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.drink1 = Drink("Lambrini", 1.80)
        # self.pub.inventory = [
        #     {"Lambrini":{
        #         "stock_count": 100,
        #         "item_price": 1.80,
        #         "alcohol_level": 6.0}
        #     },
        #     {"Lager":{
        #         "stock_count": 100,
        #         "item_price": 3.50,
        #         "alcohol_level": 3.8}
        #     },
        #     {"Vodka":{
        #         "stock_count": 100,
        #         "item_price": 2.50,
        #         "alcohol_level": 40}
        #     }
        # ]

    def test_pub_has_name(self):
        self.assertEqual('The Prancing Pony', self.pub.name)


    def test_pub_has_till_float(self):
        self.assertEqual(100.00, self.pub.till)

    def test_pub_has_drinks(self):
        self.pub.add_inventory(self.drink1)
        self.assertEqual(1 , len(self.pub.inventory))

    # MVP test 4

    def test_pub_has_money_from_sale(self):
        self.pub.add_money_to_till(self.drink1)
        self.assertEqual(101.80 , self.pub.till)

    def test_pub_can_sell_drink(self):
        customer1 = Customer("John", 100, 21)
        drink2 = Drink("Lager", 4.50)
        self.pub.sell_drink(customer1, drink2)
        self.assertEqual(95.50, customer1.wallet)
        self.assertEqual(104.50, self.pub.till)
    


    