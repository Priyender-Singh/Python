
import json
import os
import datetime
import time

class expense_tracker:

    def __init__(self,date_var,category,amount=0):
        self.date_var = str(date_var)
        self.category = category
        self.amount = int(amount)

    def to_dict(self):
        return {
            "Date" : self.date_var,
            "Category" : self.category,
            "Amount" : self.amount
        }

json_path = input("Enter Path").strip().replace("\\","/")

file = os.path.join(json_path,"expenses.json")

def load_data():
    if os.path.exists(file):
        with open(file,"r") as f:
            return json.load(f)
    return{}
        
def save_data(data):
    with open(file,"w") as f:
        return json.dump(data, f, indent=4)

exp=load_data()

while True:
    print("\n📊 Expense Tracker Menu")
    print("1. Add new expense")
    print("2. View all expenses")
    print("3. View expenses by category")
    print("4. Exit")
    choice = input("").strip()
    if not choice.isdigit() or not (0< int(choice) <5):
        continue
    
    if choice == "1":
        date_var = input("Enter date (yyyy-mm-dd) : ").strip()
        try:
            year, month, day =map(int,date_var.split("-"))
            date_var = datetime.date(year, month, day)
        except ValueError:
            print("❌ Invalid date format!")
            continue

        category = input("Enter category : ")
        if not category:
            print("❌ Category cannot be empty!")
            continue

        while True:
            amount = input("Enter amount : ")
            if amount.isdigit():
                amount = int(amount)
                break
            else:
                print("❌ Amount must be a number!")
        
        expense = expense_tracker(date_var,category,amount)
        exp[str(len(exp) + 1)] = expense.to_dict()
        save_data(exp)
        print("✅ Expense added successfully!")
        time.sleep(1)
    elif choice == "2":
        print("\n📒 All Expenses:")
        time.sleep(1)
        print("_"*50)
        if len(exp) > 0:
            for v in exp.values():
                expense = expense_tracker(v["Date"],v["Category"],v["Amount"])
                print(f"Date: {expense.date_var} | Category: {expense.category} | Amount: {expense.amount}")
                time.sleep(1)
        else:
            print("Total Expenditure : 0")
            time.sleep(1)
    elif choice == "3":
        cat=input("Enter category to check total:").strip()
        total = sum(int(v["Amount"]) for v in exp.values() if v["Category"].lower()==cat.lower())
        if total>0:
            print(f"Total spent on {cat} : {total}")
            time.sleep(2)
        else:
            print("Category not found!")
            time.sleep(2)
    else:
        print("Exiting program ...")
        time.sleep(2)
        print("_"*50)
        print("Program closed ❌")
        break

