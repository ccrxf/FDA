import os
from xml.dom import minidom
from pandas import DataFrame, Series
import numpy as np
import pandas as pd

root_dir = 'C:/Users/ccrxf/PycharmProjects/FDA/20190322'
files = os.listdir(root_dir)
ErrorFiles = []
os.chdir(root_dir)

'''
# remove error file
for xmlFile in files:
    if not os.path.isdir(xmlFile):
        try:
            tree = minidom.parse(xmlFile)
        except:
            ErrorFiles.append(xmlFile)

for ErrorFile in ErrorFiles:
    dst = month_dir + '/errordata/' +ErrorFile
    os.rename(ErrorFile, dst)
'''

'''
for xmlFile in files:
    if not os.path.isdir(xmlFile):
        print xmlFile
        DOMData = minidom.parse(xmlFile)
        detectors = DOMData.documentElement
        if detectors.hasAttribute("xmlns:xsi"):
            print "Root element : %s" % detectors.getAttribute("xmlns:xsi")

        date = detectors.getElementsByTagName('date')[0]
        print "date: %s" % date.childNodes[0].data
        time = detectors.getElementsByTagName('time')[0]
        print "time: %s" % time.childNodes[0].data
        agency = detectors.getElementsByTagName("agency")[0]
        print "agency: %s" % agency.childNodes[0].data
        dets = detectors.getElementsByTagName('detector')

        for det in dets:
            detectorID = det.getElementsByTagName('detector-Id')[0]
            print"\ndetector-Id: %s" % detectorID.childNodes[0].data

            lanes = det.getElementsByTagName('lane')
            for lane in lanes:
                laneNumber = lane.getElementsByTagName('lane-Number')[0]
                print "lane-Number %s" % laneNumber.childNodes[0].data
                laneStatus = lane.getElementsByTagName('lane-Status')[0]
                print "lane-Status %s" % laneStatus.childNodes[0].data
                laneVolume = lane.getElementsByTagName('lane-Volume')
                if laneVolume.length > 0:
                    print "lane-Volume %s" % laneVolume[0].childNodes[0].data
                laneOccupancy = lane.getElementsByTagName('lane-Occupancy')
                if laneOccupancy.length > 0:
                    print "lane-Occupancy %s" % laneOccupancy[0].childNodes[0].data
                laneSpeed = lane.getElementsByTagName('lane-Speed')
                if laneSpeed.length > 0:
                    print "lane-Speed %s" % laneSpeed[0].childNodes[0].data
'''
speedData = [[], [], [], []]
for xmlFile in files:
    if not os.path.isdir(xmlFile):
        print(xmlFile)
        DOMData = minidom.parse(xmlFile)
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

m = np.array(speedData)
np.save('speedData.npy', m)
