def update_timestamps_list(timestamps, data_point_1, data_point_2):
    timestamps_length = len(timestamps)

    if (timestamps_length > 0) and (timestamps[timestamps_length - 1]['to'] == data_point_1['timestamp']):
        timestamps[timestamps_length - 1]['to'] = data_point_2['timestamp']
        timestamps[timestamps_length - 1]['duration'] = data_point_2['timestamp'] - timestamps[timestamps_length - 1][
            'from']
    else:
        timestamps.append({'from': data_point_1['timestamp'], 'to': data_point_2['timestamp'],
                           'duration': data_point_2['timestamp'] - data_point_1['timestamp']})
    return timestamps


def calculate_bulb_glow_duration_datapoint(data_point_1, data_point_2, timestamps):
    duration = data_point_2['timestamp'] - data_point_1['timestamp']
    timestamps = update_timestamps_list(timestamps, data_point_1, data_point_2) if duration > 0 else timestamps
    return {'total_duration': duration, 'timestamps': timestamps }


def calculate_bulb_analytics(data_stream, sliding_window_size):
    data_stream_len = len(data_stream)
    sliding_window = sorted(data_stream[0:sliding_window_size], key=lambda i: i['timestamp'])
    counter_timestamp = sliding_window[0]['timestamp']
    total_bulb_on_duration = 0
    timestamps = []

    for i in range(sliding_window_size, data_stream_len):
        popped_element = sliding_window.pop(0)
        sliding_window.append(data_stream[i])
        sliding_window = sorted(sliding_window, key=lambda j: j['timestamp'])

        if popped_element['data'] == 1:
            if popped_element['timestamp'] == counter_timestamp and sliding_window[0]['data'] == 1:
                result = calculate_bulb_glow_duration_datapoint(popped_element, sliding_window[0], timestamps)

            else:
                temp = sliding_window[0]
                data_point_1 = popped_element;
                data_point_2 = {'timestamp':  temp['timestamp'] if temp['data'] == 1 else temp['timestamp'] - 1,
                                'data': 1}
                result = calculate_bulb_glow_duration_datapoint(data_point_1, data_point_2, timestamps)
                counter_timestamp = sliding_window[0]['timestamp']

            total_bulb_on_duration += result['total_duration']
            timestamps = result['timestamps']

        counter_timestamp += 1

    return {'total_bulb_on_duration': total_bulb_on_duration, 'timestamps': timestamps}