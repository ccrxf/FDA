import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np

a = np.load('npfiles/metadata.npy')
detData = a.tolist()

locations = [[], []]
for i in range(0, len(detData[0])):
    locations[0].append(float(detData[5][i]))
    locations[1].append(float(detData[6][i]))

m = Basemap(llcrnrlat=36, urcrnrlat=39, llcrnrlon=-95, urcrnrlon=-89)

for i in range(0, len(locations[0])):
    m.plot(locations[0][i], locations[1][i], marker='.', color='b')

plt.show()
