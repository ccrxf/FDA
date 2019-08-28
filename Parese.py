import os
from xml.dom import minidom
import numpy as np

root_dir = 'C:/Users/ccrxf/PycharmProjects/FDA/07/18'
files = os.listdir(root_dir)
os.chdir(root_dir)  # change the current working directory to path.
speedData = [[], [], [], []]
ErrorFiles = []

for xmlFile in files:
    if not os.path.isdir(xmlFile):
        try:     # remove error file
            DOMData = minidom.parse(xmlFile)
        except:
            ErrorFiles.append(xmlFile)
            print(xmlFile)
            continue

        try:
            print(xmlFile)
            detectors = DOMData.documentElement

            date = detectors.getElementsByTagName('date')[0]
            time = detectors.getElementsByTagName('time')[0]
            agency = detectors.getElementsByTagName("agency")[0]
            dets = detectors.getElementsByTagName('detector')

            for det in dets:
                detectorID = det.getElementsByTagName('detector-Id')[0]
                # print"\ndetector-Id: %s" % detectorID.childNodes[0].data
                if detectorID.childNodes[0].data == "MI064E009.1D":
                    lanes = det.getElementsByTagName('lane')
                    for lane in lanes:
                        laneNumber = lane.getElementsByTagName('lane-Number')[0]
                        if laneNumber.childNodes[0].data == "1":
                            laneStatus = lane.getElementsByTagName('lane-Status')[0]
                            if laneStatus.childNodes[0].data == "OK":
                                laneVolume = lane.getElementsByTagName('lane-Volume')
                                laneOccupancy = lane.getElementsByTagName('lane-Occupancy')
                                laneSpeed = lane.getElementsByTagName('lane-Speed')
                                if laneVolume.length >= 0 and laneOccupancy.length >= 0 and laneSpeed.length >= 0:
                                    speedData[0].append(time.childNodes[0].data)
                                    speedData[1].append(laneVolume[0].childNodes[0].data)
                                    speedData[2].append(laneOccupancy[0].childNodes[0].data)
                                    speedData[3].append(laneSpeed[0].childNodes[0].data)
        except IndexError:
            continue

os.mkdir(root_dir + '/errordata')
for ErrorFile in ErrorFiles:
    dst = root_dir + '/errordata/' +ErrorFile
    os.rename(ErrorFile, dst)

m = np.array(speedData)
os.chdir('C:/Users/ccrxf/PycharmProjects/FDA/npfiles')
np.save('2019_07_18.npy', m)
