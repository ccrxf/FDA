import os
import numpy as np
from scipy.interpolate import splev, splrep, BSpline
import matplotlib.pyplot as plt


def u_to_time(time_uni):
    second = int(time_uni[0:2]) * 3600 + int(time_uni[2:4]) * 60 + int(time_uni[4:6])
    return second


root_dir = 'C:/Users/ccrxf/PycharmProjects/FDA/npfiles/'
detNames = ['MI255E000.0D', 'MI270S013.6D', 'MI070E210.0D', 'MI070E243.9D', 'MI044E250.8D', 'MI044E246.6D']
files = ['20190701.npy', '20190702.npy', '20190703.npy', '20190704.npy', '20190705.npy', '20190706.npy', '20190707.npy',
         '20190708.npy', '20190709.npy', '20190710.npy', '20190711.npy', '20190712.npy', '20190713.npy', '20190714.npy',
         '20190715.npy', '20190716.npy', '20190717.npy', '20190718.npy']
dets = detNames[2:4]
fls = files[5:7]
integrate = 900
plt.figure()
plt.ylim((45, 80))
for j in range(0, len(dets)):
    os.chdir(root_dir+dets[j])
    for fl in fls:
        a = np.load(fl)
        speedData = a.tolist()
        time = speedData[1]
        speed = speedData[4]
        volume = speedData[2]

        for i in range(0, len(time)):
            time[i] = u_to_time(time[i])
            speed[i] = float(speed[i])
            volume[i] = int(volume[i])

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
        tck = splrep(time1, speed1, s=1)
        speed_spline = splev(time2, tck)
        # plt.plot(time1, speed1, '.', time2, speed_spline, linewidth=0.5, label=dets[j]+fl)
        plt.plot(time2, speed_spline, linewidth=0.5, label=dets[j] + fl)
plt.legend()
plt.show()

# pdData.to_csv('speedData.csv', encoding='gbk')
