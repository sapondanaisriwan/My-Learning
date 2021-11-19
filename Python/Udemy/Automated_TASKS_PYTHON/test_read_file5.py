import os
import datetime
import shutil

# shutil.copy(os.path.join("documents", 'ZAPI_AGL_DD.csv'), os.path.join("documents\dir", "ZAPI_AGL_DD2.csv"))
# shutil.copy2(os.path.join("documents", 'ZAPI_AGL_DD.csv'), os.path.join("documents\dir", "ZAPI_AGL_DD3.csv"))

# shutil.copytree("documents\dir\subdir", "documents\subdir2")
shutil.move(os.path.join("documents", 'ZAPI_AGL_DD2.csv'), os.path.join("documents\subdir2", 'ZAPI_AGL_DD.csv'))