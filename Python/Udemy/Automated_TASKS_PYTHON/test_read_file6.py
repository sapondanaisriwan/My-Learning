import os
import datetime
import shutil

# File
os.rename(os.path.join("documents\dir", 'file97.txt'), os.path.join("documents\dir", 'file2.txt')) # rename file

os.remove(os.path.join("documents\subdir2", "test")) # remove file

# Folder
shutil.rmtree(os.path.join("documents\subdir2")) # remove folder