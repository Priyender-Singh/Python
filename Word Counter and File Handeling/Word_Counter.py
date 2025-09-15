# Accepts a paragraph of text from the user.
# Counts how many times each word appears.
# Saves the word counts into a file called word_count.txt in the format:

import os
import string
import datetime
import textwrap
from collections import Counter

name_counter=1

folder_path=input("Enter your path : \n").strip()
# folder_path=folder_path.replace("\\","\\\\")

while True:
    folder_name=f"{name_counter}_Word_Counter_{datetime.date.today().strftime("%Y_%m_%d")}"
    full_path=os.path.join(folder_path,folder_name)
    if not os.path.exists(full_path):
        os.mkdir(full_path)
        print(f"Folder '{folder_name}' Created Successfully!!")
        break
    else:
        name_counter +=1

file_path=os.path.join(full_path,"Word_Count.txt")

paragraph=input("Write a paragraph : \n") #input from user
new_para= "".join(ch for ch in paragraph if ch not in string.punctuation) #punchutaion removed
new_para=Counter(new_para.lower().split()) # counter for each letter created
biggest_word=max(new_para, key=len)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(f"{textwrap.fill(paragraph, width=80)}\n\n")
    f.write("Below are the words and their repetation from above paragraph\n")
    f.write("_"*62)
    f.write(f"\n\n{'Words':<{len(biggest_word)}} Counts\n")
    for words,counts in new_para.items():
        f.write(f"{words.capitalize():<{len(biggest_word)}} {counts}\n")

print(f"Word counts written successfully to {file_path}")
