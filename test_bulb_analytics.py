from unittest import TestCase
from bulb_analytics import *


class CalculateBulbGlowDuration(TestCase):
    # test cases for the consecutive data points with no missing data points in between
    def test_calculate_bulb_glow_duration_when_2_consecutive_datapoints_positive(self):
        data_point_1 = {'timestamp': 1, 'data': 1}
        data_point_2 = {'timestamp': 2, 'data': 1}
        timestamps = []

        expected_timestamps = [{'from': 1, 'to': 2}]

        self.assertEqual(calculate_bulb_glow_duration(data_point_1, data_point_2, timestamps),
                         {'duration': 1, 'timestamps': expected_timestamps})

    def test_calculate_bulb_glow_duration_when_2_discrete_datapoints_positive(self):
        data_point_1 = {'timestamp': 1, 'data': 1}
        data_point_2 = {'timestamp': 5, 'data': 1}
        timestamps = []

        expected_timestamps = [{'from': 1, 'to': 5}]
        self.assertEqual(calculate_bulb_glow_duration(data_point_1, data_point_2, timestamps),
                         {'duration': 4, 'timestamps': expected_timestamps })