import numpy as np
import pandas as pd
from scipy.interpolate import splev, splrep, BSpline
import matplotlib.pyplot as plt


a = np.load('20190322/speedData.npy')
speedData = a.T.tolist()
name = ['time', 'volume', 'occupancy', 'speed']
pdData = pd.DataFrame(columns=name, data=speedData)
time = pdData['time'].tolist()
integrate = 900


def u_to_time(time_uni):
    second = int(time_uni[0:2]) * 3600 + int(time_uni[2:4]) * 60 + int(time_uni[4:6])
    return second


for i in range(0, len(time)):
    time[i] = u_to_time(time[i])

speed = pdData['speed'].astype('int').tolist()
volume = pdData['volume'].astype('int').tolist()

time1 = []
speed1 = []

b = 0
while b+integrate <= 86400:
    time300 = 0
    speed300 = 0
    not_0_t = 0
    not_0_volume = 0
    for i in range(0, len(speed)):
        if b <= time[i] < b+integrate and 0 != speed[i]:
            time300 += time[i]
            speed300 += speed[i]*volume[i]
            not_0_t += 1
            not_0_volume += volume[i]
    if not_0_t != 0:
        time1.append(time300/not_0_t)
        speed1.append(speed300 / float(not_0_volume))
    b = b+integrate


# plt.plot(time1, speed1, '*-')
# plt.show()
time2 = np.linspace(0, 85000, 2880)
tck = splrep(time1, speed1, s=5)
speed_spline = splev(time2, tck)
plt.plot(time1, speed1, '.', time2, speed_spline, linewidth=1, label='B_spline interpolation')
plt.show()



# pdData.to_csv('speedData.csv', encoding='gbk')
