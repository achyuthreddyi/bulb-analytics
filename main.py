import json
import sys

from bulb_analytics import calculate_bulb_analytics

window_size = 100

args_len = len(sys.argv)

if args_len > 1:
    data_file = open(sys.argv[1])
else:
    data_file = open('data.json')

data = json.load(data_file)
result = calculate_bulb_analytics(data, window_size)

print('The smartest Bulb was glowing for a period of ', result['total_bulb_on_duration'], 'seconds')
print('Bulb was glowing during following timestamps and for the corresponding duration')

timestamps = result['timestamps']

for i in range(len(timestamps)):
    print(timestamps[i])



#