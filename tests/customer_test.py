import unittest
from src.customer import Customer
from src.drinks import Drink

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Katie", 50.00, 28)
        self.drink1 = Drink("Lambrini", 1.80)


    def test_customer_has_name(self):
        self.assertEqual('Katie', self.customer.name)


    def test_customer_has_money(self):
        self.assertEqual(50.00, self.customer.wallet)


    def test_customer_age(self):
        self.assertEqual(28, self.customer.age)

    def test_customer_bought_drink(self):
        self.assertEqual(28, self.customer.age)

    def test_customer_can_buy_drink(self):
        self.customer.buy_drink(self.drink1)
        self.assertEqual(48.20, self.customer.wallet)


        # def test_can_pick_up_passenger_from_bus_stop(self):
            # person = Person("Guido van Rossum", 64, "Ocean Terminal")
            # person_2 = Person("Carol Willing", 50, "Meadows")
            # bus_stop = BusStop("Waverly Station")
            # bus_stop.add_to_queue(person)
            # bus_stop.add_to_queue(person_2)
            # self.bus.pick_up_from_stop(bus_stop)
            # self.assertEqual(1, self.bus.passenger_count())