import os
file = open(os.path.join("documents", 'ZAPI_AGL_DD.csv'), 'rt', encoding="tis-620",errors='ignore')

for line in file:
    PP_yyyy = line[0:4]
    PP_mm = line[4:6]
    PP_dd = line[6:8]
    processing_date = PP_dd + '/' + PP_mm + '/' + PP_yyyy
    sys_ref_no = line[239:259]
    print(sys_ref_no)

file.close()