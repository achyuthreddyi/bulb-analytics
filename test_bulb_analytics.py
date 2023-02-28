from unittest import TestCase
from bulb_analytics import *


class Test(TestCase):
    def test_calculate_bulb_analytics(self):
        self.assertEqual(calculate_bulb_analytics(), 'testing')
