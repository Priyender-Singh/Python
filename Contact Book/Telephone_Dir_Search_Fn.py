
import json
import os
import datetime

class contact_details:
    def __init__ (self,name,phone,email,seq1):
        self.name=name
        self.phone=phone
        self.email=email
        self.seq1=seq1

    def add_details(self):
        return {"Name": self.name, "Phone": self.phone, "Email": self.email}

def create_folder(path):
    COUNTER=1
    while True:
        new_folder=f"{COUNTER}_ContactBook_{datetime.date.today()}"
        full_path=os.path.join(path,new_folder)
        if not os.path.exists(full_path):
            os.mkdir(full_path)
            print(f"File '{new_folder}' Created Successfully!")
            return full_path
        COUNTER +=1

contact_book={}
seq1=0
path=input("Enter folder path to save Contact Book: \n")
save_path=create_folder(path)
while True:
    name=input("Conctact Name (Enter 'end' to stop): ").capitalize().strip()
    if name=="":
        continue
    if name.lower()=="end":
        break
    seq1 +=1
    while True:
        phone=input("Contact Number : ")
        if len(phone) == 10 and phone.isdigit():
            break
        print("Invalid number! Try again.")

    email=input("Email id : ").strip()
    contact=contact_details(name,phone,email,seq1)
    contact_book[str(seq1)] = contact.add_details()

if len(contact_book)==0:
    print("No Contact Saved")
else:
    json_file_path=os.path.join(save_path,"contacts.json")
    with open(json_file_path,"w") as f:
        json.dump(contact_book, f, indent=4)

    print(f"Contacts saved successfully at: {json_file_path}")

    with open(json_file_path,"r") as f:
        contact_dict=json.load(f)

    search_box=input("Search Name :\n").lower()

    for details in contact_dict.values():
        if details["Name"].lower() == search_box:
            print(f"Name: {details['Name']} | Phone: {details['Phone']} | Email: {details['Email']}")
            break
    else:
        print("No Contact Found")
