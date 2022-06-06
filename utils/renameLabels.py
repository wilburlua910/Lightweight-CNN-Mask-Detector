from dataclasses import replace
import os
import re

#Utility class to change the output label using regex

data_dir = '/home/wilburlua/Capstone/Detectors/yolov5-master/runs/detect/exp6'
print(data_dir)

def list_all_files(dir):
    for subdir, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(".txt"):
                print(file)
                target_file = os.path.join(subdir, file)
                print(target_file)

                with open(file=target_file, mode='r+') as f:
                    lines = f.read()
                    replaced = re.sub(r'1(?=\s\d+\.\d+){4}', '0', lines)
                    f.seek(0)
                    f.write(replaced)
                    f.truncate()
            #print(os.path.join(subdir, file))

list_all_files(dir=data_dir)