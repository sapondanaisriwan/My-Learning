import os
import datetime
file_stat = os.stat(os.path.join("documents", 'ZAPI_AGL_DD.csv'))
print(str(datetime.datetime.fromtimestamp(file_stat.st_atime))[0:19])
print(file_stat.st_size)