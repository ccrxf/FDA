import os
from xml.dom import minidom

root_dir = 'C:/Users/ccrxf/PycharmProjects/FDA/07/01'
files = os.listdir(root_dir)
ErrorFiles = []
os.chdir(root_dir)

# remove error file
for xmlFile in files:
    if not os.path.isdir(xmlFile):
        try:
            tree = minidom.parse(xmlFile)
        except:
            ErrorFiles.append(xmlFile)
            print(xmlFile)

for ErrorFile in ErrorFiles:
    dst = root_dir + '/errordata/' +ErrorFile
    os.rename(ErrorFile, dst)