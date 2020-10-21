import unittest
from scr.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Katie", 50.00, 28)

    