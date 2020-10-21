import unittest
from scr.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Katie", 50.00, 28)

    def test_customer_has_name(self):
        self.assertEqual('Katie', self.customer.customer_name)


    def test_customer_has_money(self):
        self.assertEqual(50.00, self.customer.customer_wallet)


    def test_customer_age(self):
        self.assertEqual(28, self.customer.customer_age)