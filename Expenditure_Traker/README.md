# 📊 Expense Tracker

A simple Python-based console application to track your daily expenses. All data is stored in a JSON file, allowing you to view, add, and summarize your expenses by category.

---

## 🛠 Features

1. **Add new expense**
   - Input the date (`yyyy-mm-dd`), category, and amount.
   - Stores the expense in a JSON file.

2. **View all expenses**
   - Lists all recorded expenses with date, category, and amount.
   - Shows total expenditure.

3. **View expenses by category**
   - Input a category name to get the total expenditure for that category.

4. **Exit**
   - Safely exits the program.

---

## ⚙️ How It Works

- The program uses a **class `expense_tracker`** to represent each expense with:
  - `date_var` → the date of the expense
  - `category` → category of spending
  - `amount` → expense amount

- Expenses are saved in a **JSON file** (`expenses.json`) in the folder of your choice.  

- **Data Persistence:**  
  - When the program starts, it loads existing expenses from the JSON file.
  - New expenses are appended and saved back to the file.

- **Input Validation:**  
  - Date format is validated (`yyyy-mm-dd`).
  - Amount must be numeric.
  - Category cannot be empty.

---

## 📂 JSON File Structure

Each expense is stored as a dictionary inside the JSON file:

```json
{
  "1": {
    "Date": "2025-09-19",
    "Category": "Food",
    "Amount": 250
  },
  "2": {
    "Date": "2025-09-19",
    "Category": "Transport",
    "Amount": 100
  }
}```

📝 Usage

1. Run the program:
python Expense_Tracker.py

2. Enter the path where you want the JSON file to be stored.
    - Use the menu to:
    - Add new expenses
    - View all expenses
    - Check total spending by category
    - Exit the program

⚡ Example Run
📊 Expense Tracker Menu
1. Add new expense
2. View all expenses
3. View expenses by category
4. Exit

- Add a new expense:
Enter date (yyyy-mm-dd) : 2025-09-19
Enter category : Food
Enter amount : 250
✅ Expense added successfully!

- View all expenses:
Date: 2025-09-19 | Category: Food | Amount: 250

- View expenses by category:
Enter category to check total: Food
Total spent on Food : 250

💡 Notes
1. Make sure the folder path you provide exists; the program will not create new folders.
2. The program is console-based and uses simple input/output for easy usage.

📌 Requirements
1. Python 3.x
2. Standard libraries only (json, os, datetime, time)

🏷 License
This project is open-source and free to use for personal or educational purposes.