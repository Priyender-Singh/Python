
import os
import sys
import json
import time
import shutil
import datetime
from collections import Counter


if len(sys.argv)>1:
    path = sys.argv[1]
else:
    path = input("Enter path : ").strip().replace("\\","/")

if not os.path.exists(path):
    print("Path Not Exist!")
    sys.exit(1)

metadata={}
jfile=os.path.join(path,"metadata.json")
ext=Counter(files.split(".")[-1] for files in os.listdir(path) if "." in files)

if os.path.exists(jfile):
    with open(jfile,"r") as f:
        metadata=json.load(f)
else:
    metadata={}


for i,file in enumerate(os.listdir(path)):
    src = os.path.join(path,file)
    if os.path.isfile(src):
        stat_info=os.stat(src)
        metadata[str(i+1)] = {
        "File Name" : file,
        "File extension" : os.path.splitext(file)[-1],
        "Size (kb)" : round(os.path.getsize(src)/1024,2),
        "Size (bytes)" : stat_info.st_size,
        "Created" : datetime.datetime.fromtimestamp(stat_info.st_ctime).strftime ("%Y-%m-%d %H:%M:%S"),
        "Modified" : datetime.datetime.fromtimestamp(stat_info.st_mtime).strftime ("%Y-%m-%d %H:%M:%S"),
        "Accessed" : datetime.datetime.fromtimestamp(stat_info.st_atime).strftime("%Y-%m-%d %H:%M:%S")
        }

with open(jfile,"w") as f:
    json.dump(metadata, f, indent=4)

print("✅ Metadata saved to file : metadata.json\n")
time.sleep(2)
print("--"*30)
print(f"Total files : {len(os.listdir(path))}")
time.sleep(1)
all_files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
largest_file = max(all_files, key=lambda f: os.path.getsize(os.path.join(path, f)))

print(f"Largest files : {largest_file} ({round(os.path.getsize(os.path.join(path,largest_file))/1024,2)})")
time.sleep(2)
print("📊 Folder Summary")
print("--"*30)
for k,v in ext.items():
    time.sleep(1)
    print(f"{k} : {v}\n")
print(metadata)
shutil.make_archive("metadata","zip",root_dir=os.path.join(path))