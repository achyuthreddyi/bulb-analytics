from unittest import TestCase
from bulb_analytics import *


class CalculateBulbTest(TestCase):
    def test_calculate_bulb_analytics(self):
        self.assertEqual(calculate_bulb_analytics(), 'testing')

class CalculateBulbGlowDuration(TestCase):
    # test cases for the consecutive data points with no missing data points in between
    def test_calculate_bulb_glow_duration_when_2_datapoints_positive(self):
        data_point_1 = {'timestamp': 1, 'data': 1}
        data_point_2 = {'timestamp': 2, 'data': 1}

        self.assertEqual(calculate_bulb_glow_duration(data_point_1, data_point_2), 1)

    def test_calculate_bulb_glow_duration_when_2_datapoints_negative(self):
        data_point_1 = {'timestamp': 1, 'data': 0}
        data_point_2 = {'timestamp': 2, 'data': 0}

        self.assertEqual(calculate_bulb_glow_duration(data_point_1, data_point_2), 0)

    def test_calculate_bulb_glow_duration_when_1_datapoint_negative(self):
        data_point_1 = {'timestamp': 1, 'data': 1}
        data_point_2 = {'timestamp': 2, 'data': 0}

        self.assertEqual(calculate_bulb_glow_duration(data_point_1, data_point_2), 0)



