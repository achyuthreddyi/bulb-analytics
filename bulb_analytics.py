def calculate_bulb_glow_duration(data_point_1, data_point_2):
    if data_point_1['data'] == 1 and data_point_2['data'] == 1:
        return data_point_2['timestamp'] - data_point_1['timestamp']
    return 0


def calculate_bulb_analytics(data_stream, sliding_window_size):
    data_stream_length = len(data_stream)
    total_duration = 0
    sliding_window = sorted(data_stream[0:sliding_window_size], key=lambda i: i['timestamp'])

    # if data_stream_length < sliding_window_size:
    #     for i in range (0, len(sliding_window) - 1):
    #         total_duration +=
