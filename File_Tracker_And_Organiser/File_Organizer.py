
import os
import shutil
import sys

if len(sys.argv)>1:
    path=sys.argv[1]
else:
    path=input("Enter path :\n").strip().replace("\\","/")

if not os.path.exists(path):
    print(f"Path does not exists : {path}")
    sys.exit(1)

extension=set()

# 1. Creating Folder Name via extensions
for files in os.listdir(path):
    new_files = os.path.join(path,files)
    if os.path.isfile(new_files):
        if "." in files:
            extension.add(files.split(".")[-1])
        else:
            extension.add("Other")

# 2. Creating folders using extension
for items in extension:
    folder = os.path.join(path,items)
    if not os.path.exists(folder):
        os.mkdir(folder)

# 3. Moving files into required folder

for files in os.listdir(path):
    src = os.path.join(path, files)
    if os.path.isfile(src):
        ext = files.split(".")[-1] if "." in files else "Other"
        dest = os.path.join(path, ext, files)
        shutil.move(src, dest)

print("✅ Files organized successfully!")

