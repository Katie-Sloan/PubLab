import unittest
from scr.drinks import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drinks = Drink("Lambrini", 1.80)

    def test_drink_has_name(self):
        self.assertEqual('Lambrini', self.drinks.drink_name)


    def test_drink_has_price(self):
        self.assertEqual(1.80, self.drinks.drink_price)