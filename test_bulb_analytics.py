from unittest import TestCase
from bulb_analytics import *


# class CalculateBulbGlowDuration(TestCase):
#     # test cases for the consecutive data points with no missing data points in between
#     def test_calculate_bulb_glow_duration_when_2_consecutive_datapoints_positive(self):
#         data_point_1 = {'timestamp': 1, 'data': 1}
#         data_point_2 = {'timestamp': 2, 'data': 1}
#         timestamps = []
#
#         expected_timestamps = [{'from': 1, 'to': 2}]
#
#         self.assertEqual(calculate_bulb_glow_duration(data_point_1, data_point_2, timestamps),
#                          {'duration': 1, 'timestamps': expected_timestamps})
#
#     def test_calculate_bulb_glow_duration_when_2_discrete_datapoints_positive(self):
#         data_point_1 = {'timestamp': 1, 'data': 1}
#         data_point_2 = {'timestamp': 5, 'data': 1}
#         timestamps = []
#
#         expected_timestamps = [{'from': 1, 'to': 5}]
#         self.assertEqual(calculate_bulb_glow_duration(data_point_1, data_point_2, timestamps),
#                          {'duration': 4, 'timestamps': expected_timestamps})


class CalculateBulbAnalytics(TestCase):
    def test_calculate_bulb_analytics_with_ordered_and_no_positive_data(self):
        data_list = [{'timestamp': 1, 'data': 0}, {'timestamp': 2, 'data': 0},
                     {'timestamp': 3, 'data': 0}, {'timestamp': 4, 'data': 0},
                     {'timestamp': 5, 'data': 0}, {'timestamp': 6, 'data': 0},
                     {'timestamp': 7, 'data': 0}, {'timestamp': 8, 'data': 0},
                     {'timestamp': 9, 'data': 0}]
        window_size = 3

        result = {'total_bulb_on_duration': 0,
                  'timestamps': []}

        self.assertEqual(calculate_bulb_analytics(data_list, window_size), result)

    def test_calculate_bulb_analytics_with_ordered_and_alternating_positive_data(self):
        data_list = [{'timestamp': 1, 'data': 1}, {'timestamp': 2, 'data': 0},
                     {'timestamp': 3, 'data': 1}, {'timestamp': 4, 'data': 0},
                     {'timestamp': 5, 'data': 1}, {'timestamp': 6, 'data': 0},
                     {'timestamp': 7, 'data': 1}, {'timestamp': 8, 'data': 0},
                     {'timestamp': 9, 'data': 1}]
        window_size = 3

        result = {'total_bulb_on_duration': 0,
                  'timestamps': []}

        self.assertEqual(calculate_bulb_analytics(data_list, window_size), result)

    def test_calculate_bulb_analytics_with_ordered_and_no_missing_data(self):
        data_list = [{'timestamp': 1, 'data': 1}, {'timestamp': 2, 'data': 1},
                     {'timestamp': 3, 'data': 1}, {'timestamp': 4, 'data': 0},
                     {'timestamp': 5, 'data': 1}, {'timestamp': 6, 'data': 1},
                     {'timestamp': 7, 'data': 1}, {'timestamp': 8, 'data': 0},
                     {'timestamp': 9, 'data': 0}]
        window_size = 3

        result = {'total_bulb_on_duration': 4,
                  'timestamps': [{'from': 1, 'to': 3, 'duration': 2},
                                 {'from': 5, 'to': 7, 'duration': 2}]}

        self.assertEqual(calculate_bulb_analytics(data_list, window_size), result)

    def test_calculate_bulb_analytics_with_unordered_and_no_missing_data(self):
        data_list = [{'timestamp': 1, 'data': 1}, {'timestamp': 3, 'data': 1},
                     {'timestamp': 2, 'data': 1}, {'timestamp': 4, 'data': 0},
                     {'timestamp': 5, 'data': 1}, {'timestamp': 7, 'data': 1},
                     {'timestamp': 6, 'data': 1}, {'timestamp': 8, 'data': 0},
                     {'timestamp': 9, 'data': 0}]
        window_size = 3

        result = {'total_bulb_on_duration': 4,
                  'timestamps': [{'from': 1, 'to': 3, 'duration': 2},
                                 {'from': 5, 'to': 7, 'duration': 2}]}

        self.assertEqual(calculate_bulb_analytics(data_list, window_size), result)

    def test_calculate_bulb_analytics_with_ordered_and_missing_data(self):
        data_list = [{'timestamp': 1, 'data': 1}, {'timestamp': 3, 'data': 1},
                     {'timestamp': 4, 'data': 0}, {'timestamp': 5, 'data': 1},
                     {'timestamp': 7, 'data': 1}, {'timestamp': 8, 'data': 0},
                     {'timestamp': 9, 'data': 0}]
        window_size = 3

        result = {'total_bulb_on_duration': 4,
                  'timestamps': [{'from': 1, 'to': 3, 'duration': 2},
                                 {'from': 5, 'to': 7, 'duration': 2}]}

        self.assertEqual(calculate_bulb_analytics(data_list, window_size), result)

    def test_calculate_bulb_analytics_with_unordered_and_missing_data(self):
        data_list = [{'timestamp': 3, 'data': 1}, {'timestamp': 1, 'data': 1},
                    {'timestamp': 4, 'data': 1},
                    {'timestamp': 5, 'data': 0}, {'timestamp': 7, 'data': 0},
                    {'timestamp': 8, 'data': 1}, {'timestamp': 9, 'data': 0}]
        window_size = 3

        result = {'total_bulb_on_duration': 3,
                  'timestamps': [{'duration': 3, 'from': 1, 'to': 4}]}

        self.assertEqual(calculate_bulb_analytics(data_list, window_size), result)
