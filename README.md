# Bulb Analytics

### Problem Statement

Given a smartest bulb, which pushes the status of glowing to the cloud continuously.
Our task is to analyze the data and get total time the bulb was glowing. All the data would reach 
to the cloud server within 100 seconds/points. If the data is not received within 100 seconds it is assumed
that data is lost, and the status remains same of the previous timestamp.

### Input Format

Input format is json file which contains an array of datapoint file.
Each datapoint contains the timestamp and status of the bulb.

### Assumptions
1. The data given to the program is clean and does not contain any junk data. However, data can be missing 
and can be unordered.
2. In the problem statement, It is mentioned that data would reach the server within 100 seconds/points. It can be deduced that the any data point can be found in the next 100 points (Unorderliness of data can happen only in the window of 100 data points).

### Approach to solve the problem used.

-  Since the data can be in any order and need not hit the server in the chronological order. We can leverage to the fact that any data point if it is hitting the server would be in the next 100 points from the current timestamp. So we can use this to convert the problem into a sliding window problem, where in 100 lies as the window size to do our operation.
- In each iteration we pop the element and add a new element in the given sliding window which would be sorted according to the timestamp.
<img width="711" alt="demo" src="https://user-images.githubusercontent.com/35003947/222177783-53066ca6-35d4-4d1d-9a49-694a02770ccb.png">

### Running the test file
```commandline
python -m unittest test test_bulb_analytics.py
```

### Running the Program

```commandline
python main.py
```
By default the program runs the data.json file.To run the program for a custom data file using the following command.
```commandline
python main.py 'filename'
```

