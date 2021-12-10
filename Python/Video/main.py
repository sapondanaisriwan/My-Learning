# -- coding: utf-8 --

import json
import math
import os

def convert_json_to_srt(json_files_path):    
    json_files = os.listdir(json_files_path)
    srt_files_path = os.path.join(json_files_path, 'srt') #Change the path of the subtitle file after the suffix    
    isExists = os.path.exists(srt_files_path)
    if not isExists:
        os.mkdir(srt_files_path)
    
    for json_file in json_files:        
        file_name = json_file.replace(json_file[-5:], '.srt') #Change the suffix of the converted subtitles
        file = ''  #  This variable is used to save data
        i = 1
        #  Modify the file location here and add utf-8 to avoid errors when processing Chinese
        with open(os.path.join(json_files_path, json_file), encoding='utf-8') as f:
            datas = json.load(f)#  Load file data
            f.close()
                    
        for data in datas['body']:
            start = data['from']  #  Get start time
            stop = data['to']  #  Get end time
            content = data['content']  #  Get subtitle content
            file += '{}\n'.format(i)  #  Join the serial number
            hour = math.floor(start) // 3600
            minute = (math.floor(start) - hour * 3600) // 60
            sec = math.floor(start) - hour * 3600 - minute * 60
            minisec = int(math.modf(start)[0] * 100)  #  Processing start time
            file += str(hour).zfill(2) + ':' + str(minute).zfill(2) + ':' + str(sec).zfill(2) + ',' + str(minisec).zfill(2)  #  Fill the number with 0 and write in the format
            file += ' --> '
            hour = math.floor(stop) // 3600
            minute = (math.floor(stop) - hour * 3600) // 60
            sec = math.floor(stop) - hour * 3600 - minute * 60
            minisec = abs(int(math.modf(stop)[0] * 100 - 1))  #  The minus 1 here is to prevent two subtitles from appearing at the same time
            file += str(hour).zfill(2) + ':' + str(minute).zfill(2) + ':' + str(sec).zfill(2) + ',' + str(minisec).zfill(2)
            file += '\n' + content + '\n\n'  #  Add subtitle text
            i += 1
        with open(os.path.join(srt_files_path, file_name), 'w', encoding='utf-8') as f:
            f.write(file)  #  Write data to file
                        
if __name__ == '__main__':   
    json_folder_path = "D:\My Project\My Learning\Python\Video" #The path of the json subtitle file (note the format of the path)
    convert_json_to_srt(json_folder_path)