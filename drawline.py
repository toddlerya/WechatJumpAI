#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: toddler


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def get_data(file_name):
    x_list = list()
    y_list = list()
    data = pd.read_csv(file_name)
    distance_array = []
    press_time_array = []
    for distance, press_time in zip(data['Distance'], data['Press_time']):
        distance_array.append([float(distance.strip().strip('[]'))])
        press_time_array.append([float(press_time.strip().strip('[]'))])

    for i in data.get_values():
        __x = eval(i[0])[0]
        __y = eval(i[1])[0]
        x_list.append(__x)
        y_list.append(__y)

    return distance_array, press_time_array, x_list, y_list



csv_file = "jump_range.csv"

regr = LinearRegression()

plt.close()
plt.figure()
plt.grid(True)
plt.title('LinearRegression [Distance = k * PressTime + b]')
plt.xlabel("Distance(pixel point)")
plt.ylabel("PressTime(ms)")

distances, press_times, x_list, y_list = get_data(csv_file)
regr.fit(distances, press_times)
predict_press_time = regr.predict(distances)
# 截距 b
intercept = regr.intercept_
# 斜率值 k
coefficient = regr.coef_
equation = "Distance = {0} * PressTime + {1}".format(coefficient[0][0], intercept[0])
print equation

plt.scatter(x_list, y_list, edgecolors='blue')
plt.plot(distances, predict_press_time, color='red', linewidth=2, label=equation)
plt.legend()
plt.savefig("LinearRegression", dpi=1920)
plt.show()
