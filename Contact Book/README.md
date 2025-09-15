# 📖 PyContactBook

A simple **Contact Book** application written in Python.  
It allows you to add, store, and search contacts. Contacts are saved in a structured **JSON file** inside a uniquely created folder (based on date).

---

## ✨ Features
- Add multiple contacts with **Name, Phone, Email**
- Validates phone number (must be 10 digits)
- Skips empty names automatically
- Automatically creates a new folder for each run
- Saves contacts into `contacts.json`
- Search contacts by name (case-insensitive)

---

## 🛠️ How It Works
1. Run the script:
   ```bash
   python contact_book.py

2. Enter a folder path where you want to save your Contact Book.
3. Enter contact details (Name, Phone, Email).
- Enter 'end' when you are done.
4. The program will create a new folder: `1_ContactBook_YYYY-MM-DD/contacts.json`
5. Search contacts by name.

**📂 Example contacts.json**

{
    "1": {
        "Name": "Amit Sharma",
        "Phone": "9876543210",
        "Email": "amit.sharma@mail.com"
    },
    "2": {
        "Name": "Priya Verma",
        "Phone": "9123456789",
        "Email": "priya.verma@mail.com"
    }
}

**🔍 Example Search**
Search Name :
amit sharma
**OUTPUT**
`Name: Amit Sharma | Phone: 9876543210 | Email: amit.sharma@mail.com`

**If not found:**
`No Contact Found`

**If no contacts in Contact Book:**
`No Contact Saved`