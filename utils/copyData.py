from email.mime import base
from pathlib import Path
import os
import shutil

def list_all_files(dir, target_dir):
    for subdir, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(".jpg"):
                print(file)
                target_file = os.path.join(subdir, file)
                print(target_file)
                shutil.copy(target_file, target_dir)
            #print(os.path.join(subdir, file))


# base_path = "/home/wilburlua/CMFD"

base_path = "/home/wilburlua/Capstone/IMFD"

#Change the subdirectory to any "Pt-1, Pt-2 etc."
#src_dir = os.path.join(base_path, "Pt-1")
src_dir = os.path.join(base_path, "Pt-2")
target_dir = os.path.join(base_path, "IMFD_Compiled")


list_all_files(src_dir, target_dir= target_dir)
