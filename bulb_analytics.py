def calculate_bulb_glow_duration(data_point_1, data_point_2, timestamps):
    if (len(timestamps)) > 0 and (timestamps[len(timestamps) - 1]['to'] == data_point_1['timestamp']):
        timestamps_last_index = len(timestamps) - 1
        timestamps[timestamps_last_index]['to'] = data_point_2['timestamp']
        timestamps[timestamps_last_index]['duration'] = data_point_2['timestamp'] - timestamps[timestamps_last_index][
            'from']
    else:
        timestamps.append({'from': data_point_1['timestamp'],
                           'to': data_point_2['timestamp']})

    return {'duration': data_point_2['timestamp'] - data_point_1['timestamp'],
            'timestamps': timestamps}


def calculate_bulb_analytics(data_stream, sliding_window_size):
    data_stream_length = len(data_stream)
    total_duration = 0
    sliding_window = sorted(data_stream[0:sliding_window_size], key=lambda i: i['timestamp'])

    # if data_stream_length < sliding_window_size:
    #     for i in range (0, len(sliding_window) - 1):
    #         total_duration +=
