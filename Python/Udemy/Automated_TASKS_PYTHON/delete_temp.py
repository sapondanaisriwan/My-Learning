import os
import time
import shutil
import xml.etree.ElementTree as ET
from datetime import date
def remove_file(var_PathToDeleteFile, os, current_time, var_DaysToKeepFile):
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
            except OSError:
                pass

def get_local_time():
    local_time = str(time.ctime(time.time()))[11:20] # format current time to ctime [ctime = create time]
    return local_time


var_daysToKeepFile = '0'
var_PathToDeleteFile = "C:\Windows\Temp"
var_PathToDeleteFile2 = os.path.expanduser('~') + "\AppData\Local\Temp"
var_PathToDeleteFile3 = "C:\Windows\Prefetch"
var_path_path_source = os.getcwd() # print real path

current_time = time.time()
today = str(date.today())
today_date_current = int(today[8:10])
remove_file(var_PathToDeleteFile, os, current_time, var_daysToKeepFile)
remove_file(var_PathToDeleteFile2, os, current_time, var_daysToKeepFile)
remove_file(var_PathToDeleteFile3, os, current_time, var_daysToKeepFile)
