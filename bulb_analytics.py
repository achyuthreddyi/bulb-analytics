def update_array(timestamps, data_point_1, data_point_2):
    timestamps_length = len(timestamps)

    if timestamps_length > 0 and timestamps[timestamps_length - 1]['to'] == data_point_1['timestamp']:
        timestamps[timestamps_length - 1]['to'] = data_point_2['timestamp']
        timestamps[timestamps_length - 1]['duration'] = data_point_2['timestamp'] - timestamps[timestamps_length - 1][
            'from']
    else:
        timestamps.append({'from': data_point_1['timestamp'], 'to': data_point_2['timestamp'],
                           'duration': data_point_2['timestamp'] - data_point_1['timestamp']})
    return timestamps


def calculate_bulb_glow_duration_1(data_point_1, data_point_2, timestamps):
    bulb_on_timestamps = {'total_duration': 0, 'timestamps': []}

    if data_point_1['data'] == 1:
        bulb_on_timestamps['total_duration'] += data_point_2['timestamp'] - data_point_1['timestamp']
        bulb_on_timestamps['timestamps'] = update_array(timestamps, data_point_1, data_point_2)
    return bulb_on_timestamps


def calculate_bulb_analytics(data_stream, sliding_window_size):
    data_stream_len = len(data_stream)
    sliding_window = sorted(data_stream[0:sliding_window_size], key=lambda i: i['timestamp'])
    counter_timestamp = sliding_window[0]['timestamp']
    total_bulb_on_duration = 0
    timestamps = []

    for i in range(sliding_window_size, data_stream_len):
        print('counter_timestamp', counter_timestamp)
        popped_element = sliding_window.pop(0)
        sliding_window.append(data_stream[i])
        sliding_window = sorted(sliding_window, key=lambda j: j['timestamp'])

        if popped_element['timestamp'] == counter_timestamp:

            if sliding_window[0]['data'] == popped_element['data']:
                result = calculate_bulb_glow_duration_1(popped_element, sliding_window[0], timestamps)
                total_bulb_on_duration += result['total_duration']
                timestamps = result['timestamps']
        else:
            new_data_point = {'timestamp': sliding_window[0]['timestamp'] - 1, 'data': popped_element['data']}
            print('new_data_point', new_data_point)
            result = calculate_bulb_glow_duration_1(popped_element, new_data_point, timestamps)
            total_bulb_on_duration += result['total_duration']
            timestamps = result['timestamps']
            counter_timestamp = sliding_window[0]['timestamp']

        counter_timestamp += 1
    return {'total_bulb_on_duration': total_bulb_on_duration, 'timestamps': timestamps}