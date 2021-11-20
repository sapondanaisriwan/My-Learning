import datetime
import os
import time
import shutil
import xml.etree.ElementTree as ET
from datetime import date

def remove_file(var_PathToDeleteFile, os, var_PathToPlaceLog, log_daily, current_time, var_DaysToKeepFile):
    print(len(os.listdir(var_PathToDeleteFile)))
    if len(os.listdir(var_PathToDeleteFile)) == 0:
        return

    for file in os.listdir(var_PathToDeleteFile):
        path_file = os.path.join(var_PathToDeleteFile, file)
        creation_time = os.path.getctime(path_file)
        if (current_time - creation_time) // (24*3600) >= int(var_DaysToKeepFile):
            try:
                if os.path.isfile(path_file):
                    os.remove(path_file)
                elif os.path.isdir(path_file):
                    shutil.rmtree(path_file)
                log_transaction(var_PathToPlaceLog, log_daily, "a", "Removing file" + file)
            except OSError:
                pass
    
    log_transaction(var_PathToPlaceLog, log_daily, "a", "Removing file from local success" + file)

def log_transaction(var_PathToPlaceLog, log_daily, mode_write_file, string_to_write_log): # เขียน log
    today = str(date.today())
    result_log_daily = open(os.path.join(var_PathToPlaceLog, log_daily), mode_write_file, encoding="tis-620",errors='ignore') # open = สร้างไฟล์หรือเปิดไฟล์
    result_log_daily.write(today + get_local_time() + ':' + string_to_write_log + '\n')
    result_log_daily.close()

def get_local_time():
    local_time = str(time.ctime(time.time()))[11:20] # format current time to ctime [ctime = create time]
    return local_time


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

current_time = time.time()
today = str(date.today())
today_date_current = int(today[8:10])

log_daily = "log_daily_alert_line_" + str(today_date_current) + ".txt"
log_transaction(var_PathToPlaceLog, log_daily, "w+", "Start Housekeeping File")
log_transaction(var_PathToPlaceLog, log_daily, "a", "Destination Path for housekeeper is" + var_PathToDeleteFile)
remove_file(var_PathToDeleteFile, os, var_PathToPlaceLog, log_daily, current_time, var_daysToKeepFile)