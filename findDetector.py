import os
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
import pandas as pd

a = np.load('npfiles/metadata.npy')
detData = a.tolist()

detData_in_I44 = [[], [], [], [], [], [], []]
detData_in_I70 = [[], [], [], [], [], [], []]
detData_in_I270 = [[], [], [], [], [], [], []]
b = len(detData[0])
for i in range(0, b):
    if detData[2][i] == 'I44':
        for c in range(0, 7):
            detData_in_I44[c].append(detData[c][i])
    if detData[2][i] == 'I70':
        for c in range(0, 7):
            detData_in_I70[c].append(detData[c][i])
    if detData[2][i] == 'I270':
        for c in range(0, 7):
            detData_in_I270[c].append(detData[c][i])

m = Basemap(llcrnrlat=36, urcrnrlat=39, llcrnrlon=-95, urcrnrlon=-89)

# map of I44
for i in range(0, len(detData_in_I44[0])):
    m.plot(float(detData_in_I44[5][i]), float(detData_in_I44[6][i]), marker='.', color='b')

for i in range(0, len(detData_in_I70[0])):
    m.plot(float(detData_in_I70[5][i]), float(detData_in_I70[6][i]), marker='.', color='y')

for i in range(0, len(detData_in_I270[0])):
    m.plot(float(detData_in_I270[5][i]), float(detData_in_I270[6][i]), marker='.', color='k')

lons = [-90.677931, -90.243148804, -90.244003296, -90.678497314, -90.338798523, -90.448501587, -90.2964]
lats = [38.505837, 38.617271423, 38.685199738, 38.803001404, 38.503200531, 38.655601501, 38.77173]
m.scatter(lons, lats, marker='o', c='', edgecolors='r', s=100)

plt.show()


'''
# save as csv
name = ['detectorId', 'dotId', 'onStreetName', 'onDirection', 'atCrossStreet', 'onLongitude', 'onLatitude']
pdData = pd.DataFrame(index=name, data=detData_in_I44)
os.chdir('C:/Users/ccrxf/PycharmProjects/FDA/detectorsLocation')
pdData.to_csv('detectors_in_I44.csv')

pdData1 = pd.DataFrame(index=name, data=detData)
pdData1.to_csv('detectorsLocation.csv')

'''