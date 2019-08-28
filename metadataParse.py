from xml.dom import minidom
import numpy as np
import os


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False


metaData = minidom.parse("07/01/2019_0701_metadata.xml")
detectors = metaData.documentElement

date = detectors.getElementsByTagName('date')[0]
time = detectors.getElementsByTagName('time')[0]
agency = detectors.getElementsByTagName('agency')[0]

detData = [[], [], [], [], [], [], []]

dets = detectors.getElementsByTagName('detector')

for det in dets:
    detectorId = det.getElementsByTagName('detectorId')[0].childNodes[0].data
    dotId = det.getElementsByTagName('dotId')[0].childNodes[0].data

    try:
        linkLocation = det.getElementsByTagName('linkLocation')[0]
        crossStreets = linkLocation.getElementsByTagName('crossStreets')[0]
        onStreetName = crossStreets.getElementsByTagName('onStreetName')[0].childNodes[0].data
        onDirection = crossStreets.getElementsByTagName('onDirection')[0].childNodes[0].data
        atCrossStreet = crossStreets.getElementsByTagName('atCrossStreet')[0].childNodes[0].data
        onLongitude = crossStreets.getElementsByTagName('onLongitude')[0].childNodes[0].data
        onLatitude = crossStreets.getElementsByTagName('onLatitude')[0].childNodes[0].data
    except IndexError:
        continue

    if is_number(onLongitude) and is_number(onLatitude):
        if float(onLongitude) != 0 and float(onLatitude) != 0:
            detData[0].append(str(detectorId))
            detData[1].append(str(dotId))
            detData[2].append(str(onStreetName))
            detData[3].append(str(onDirection))
            detData[4].append(str(atCrossStreet))
            detData[5].append(float(onLongitude))
            detData[6].append(float(onLatitude))

# print min(detData[5]), max(detData[5]), min(detData[6]), max(detData[6])

'''
# save npfile
metaFile = np.array(detData)
os.chdir('C:/Users/ccrxf/PycharmProjects/FDA/npfiles')
np.save('metadata.npy', metaFile)
'''




