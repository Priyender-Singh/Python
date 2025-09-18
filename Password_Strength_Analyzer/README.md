# 🔑 Password Strength Checker

A simple Python project that analyzes the strength of a user’s password and provides **suggestions** to make it stronger.

---

## 🚀 Features
- Checks password against **5 conditions**:
  1. At least 8 characters long
  2. Contains at least one uppercase letter
  3. Contains at least one lowercase letter
  4. Contains at least one digit
  5. Contains at least one special character (`!@#$%^&*...`)

- Classifies password strength as:
  - **Weak** → if only 1–2 conditions are met
  - **Moderate** → if 3–4 conditions are met
  - **Strong** → if all 5 conditions are met

- Provides **personalized suggestions**  
  Example:  

**Suggestion:**`Add more uppercase and special chars.`

- Uses **decorators** for clean separation between:
- Password analysis
- Suggestions logic

- Adds a **checking animation**:
`🔑 Checking password...`


---

## 🛠️ Installation & Usage

1. Clone the repository:
 ```bash
 git clone 
 cd password-strength-checker

python password_checker.py

 💻 Example Run

Enter Password : hello123
🔑 Checking password...
____________________________________________________________
Strength : Moderate
Suggestion: Add more uppercase and special chars.
