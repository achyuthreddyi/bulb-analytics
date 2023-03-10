from unittest import TestCase
from bulb_analytics import *


class UpdateTimestampsList(TestCase):
    def test_update_timestamps_list_when_empty_list_passed(self):
        timestamps = []
        data_point_1 = {'timestamp': 1, 'data': 1}
        data_point_2 = {'timestamp': 5, 'data': 1}

        expected_timestamps = [{'duration': 4, 'from': 1, 'to': 5}]

        self.assertEqual(update_timestamps_list(timestamps, data_point_1, data_point_2),
                         expected_timestamps)

    def test_update_timestamps_list_when_nonempty_list_passed_without_overlapping_data(self):
        timestamps = [{'duration': 2, 'from': 1, 'to': 3}]
        data_point_1 = {'timestamp': 6, 'data': 1}
        data_point_2 = {'timestamp': 9, 'data': 1}

        expected_timestamps = [{'duration': 2, 'from': 1, 'to': 3},
                               {'duration': 3, 'from': 6, 'to': 9}]

        self.assertEqual(update_timestamps_list(timestamps, data_point_1, data_point_2),
                         expected_timestamps)

    def test_update_timestamps_list_when_nonempty_list_passed_with_overlapping_data(self):
        timestamps = [{'duration': 2, 'from': 1, 'to': 3}]
        data_point_1 = {'timestamp': 3, 'data': 1}
        data_point_2 = {'timestamp': 9, 'data': 1}

        expected_timestamps = [{'duration': 8, 'from': 1, 'to': 9}]

        self.assertEqual(update_timestamps_list(timestamps, data_point_1, data_point_2),
                         expected_timestamps)


class CalculateBulbGlowDuration(TestCase):
    # test cases for the consecutive data points with no missing data points in between
    def test_calculate_bulb_glow_duration_when_2_consecutive_datapoints_positive(self):
        data_point_1 = {'timestamp': 1, 'data': 1}
        data_point_2 = {'timestamp': 2, 'data': 1}
        timestamps = []

        expected_output = {'timestamps': [{'duration': 1, 'from': 1, 'to': 2}], 'total_duration': 1}

        self.assertEqual(calculate_bulb_glow_duration_in_datapoint(data_point_1, data_point_2, timestamps),
                         expected_output)

    def test_calculate_bulb_glow_duration_when_2_discrete_datapoints_positive(self):
        data_point_1 = {'timestamp': 1, 'data': 1}
        data_point_2 = {'timestamp': 5, 'data': 1}
        timestamps = []

        expected_output = {'timestamps': [{'duration': 4, 'from': 1, 'to': 5}], 'total_duration': 4}

        self.assertEqual(calculate_bulb_glow_duration_in_datapoint(data_point_1, data_point_2, timestamps),
                         expected_output)


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
