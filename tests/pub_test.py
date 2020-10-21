import unittest
from src.pub import Pub
from src.drinks import Drink

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

    def test_customer_can_buy_drink(self):
        pass
    