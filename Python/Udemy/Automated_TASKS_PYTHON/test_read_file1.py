import os
for path_file, dirs, files in os.walk("documents"):
    for file in files:
        print(path_file, file)
        full_file_path = os.path.join(path_file, file)
        print(type(full_file_path))