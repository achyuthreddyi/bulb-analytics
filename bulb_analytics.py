def calculate_bulb_glow_duration(data_point_1, data_point_2, timestamps):
    print('error in here')
    if (len(timestamps)) > 0 and (timestamps[len(timestamps) - 1]['to'] == data_point_1['timestamp']):
        timestamps_last_index = len(timestamps) - 1
        timestamps[timestamps_last_index]['to'] = data_point_2['timestamp']
        timestamps[timestamps_last_index]['duration'] = data_point_2['timestamp'] - timestamps[timestamps_last_index][
            'from']
    else:
        timestamps.append({'from': data_point_1['timestamp'], 'to': data_point_2['timestamp'],
                           'duration': data_point_2['timestamp'] - data_point_1['timestamp']})
    print ({'duration': data_point_2['timestamp'] - data_point_1['timestamp'],
            'timestamps': timestamps})
    return {'duration': data_point_2['timestamp'] - data_point_1['timestamp'],
            'timestamps': timestamps}


def calculate_bulb_analytics(data_stream, sliding_window_size):
    data_stream_length = len(data_stream)
    total_bulb_on_duration = 0
    timestamps = []
    sliding_window = sorted(data_stream[0:sliding_window_size], key=lambda i: i['timestamp'])

    for i in range(sliding_window_size, data_stream_length):
        popped_element = sliding_window.pop(0)
        sliding_window.append(data_stream[i])
        # TODO: Need not sort everytime rather you can place the new element in its place
        sliding_window = sorted(sliding_window, key=lambda j: j['timestamp'])

        if popped_element['data'] == 1 and sliding_window[0]['data'] == 1:
            result = calculate_bulb_glow_duration(popped_element, sliding_window[0], timestamps)
            total_bulb_on_duration += result['duration']
            timestamps = result['timestamps']

    return {'total_bulb_on_duration': total_bulb_on_duration, 'timestamps': timestamps}

