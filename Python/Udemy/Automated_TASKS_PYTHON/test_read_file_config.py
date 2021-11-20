import os
import xml.etree.ElementTree as ET

file_config = 'automated_task_file.config'
root = ET.parse(file_config).getroot()

var_PathToPlaceLog = ""
var_PathToDeleteFile = ""
var_daysToKeepFile = ""
var_path_path_source = os.getcwd() # print real path

for data in root:
    for detail in data:
        if detail.get('key') == "PathToPlaceLog":
            var_PathToPlaceLog = var_path_path_source + detail.get('value')
        elif detail.get('key') == "PathToDeleteFile":
            var_PathToDeleteFile = detail.get('value')
        elif detail.get('key') == "DaysToKeepFile":
            var_daysToKeepFile = detail.get('value')
#         print(detail.get('key'), detail.get('value'))

print(var_PathToPlaceLog, var_PathToDeleteFile, var_daysToKeepFile)