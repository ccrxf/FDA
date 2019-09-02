import os
from xml.dom import minidom
import numpy as np


def get_branches_dir(root_dir):
    branches_dir = []
    folds = os.listdir(root_dir)
    while folds:
        branch_dir = root_dir + '/' + folds.pop()
        branches_dir.append(branch_dir)
    return branches_dir


def tolist(xml, detname):
    try:
        data = minidom.parse(xml)
    except:
        print('parse error')
        ErrorFiles.append(xml)
        return

    detectors = data.documentElement
    date = detectors.getElementsByTagName('date')[0].childNodes[0].data
    time = detectors.getElementsByTagName('time')[0].childNodes[0].data
    dets = detectors.getElementsByTagName('detector')
    laneVolume = 0
    laneOccupancy = 0
    laneSpeed = 0
    for det in dets:
        try:
            detectorID = det.getElementsByTagName('detector-Id')[0]
        except IndexError:
            continue
        # print"\ndetector-Id: %s" % detectorID.childNodes[0].data
        if detectorID.childNodes[0].data in detname:
            lanes = det.getElementsByTagName('lane')
            for lane in lanes:
                # laneNumber = lane.getElementsByTagName('lane-Number')[0]
                laneStatus = lane.getElementsByTagName('lane-Status')[0]
                if laneStatus.childNodes[0].data == "OK":
                    try:
                        laneVolume += int(lane.getElementsByTagName('lane-Volume')[0].childNodes[0].data)
                        laneOccupancy += int(lane.getElementsByTagName('lane-Occupancy')[0].childNodes[0].data) * int(lane.getElementsByTagName('lane-Volume')[0].childNodes[0].data)
                        laneSpeed += int(lane.getElementsByTagName('lane-Speed')[0].childNodes[0].data) * int(lane.getElementsByTagName('lane-Volume')[0].childNodes[0].data)
                    except IndexError:
                        break
                else:
                    break

            if laneVolume > 0:
                for i in range(0, len(detname)):
                    if detectorID.childNodes[0].data == detname[i]:
                        c = i
                detectorData[c][0].append(date)
                detectorData[c][1].append(time)
                detectorData[c][2].append(laneVolume)
                detectorData[c][3].append(laneOccupancy/float(laneVolume))
                detectorData[c][4].append(laneSpeed/float(laneVolume))


month_dir = 'C:/Users/ccrxf/PycharmProjects/FDA/07'
os.chdir(month_dir)  # change the current working directory to path.
day_dir = get_branches_dir(month_dir)
detNames = ['MI255E000.0D', 'MI270S013.6D', 'MI070E210.0D', 'MI070E243.9D', 'MI044E250.8D', 'MI044E246.6D']
ErrorFiles = []
for dayFile in day_dir:
    detectorData = [[[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []]]
    xmlFiles = get_branches_dir(dayFile)
    for xml in xmlFiles:
        if not os.path.isdir(xml):
            print(xml)
            tolist(xml, detNames)

    for i in range(0, len(detNames)):
        m = np.array(detectorData[i])
        os.chdir('C:/Users/ccrxf/PycharmProjects/FDA/npfiles/'+detNames[i])
        np.save(detectorData[0][0][0]+'.npy', m)
