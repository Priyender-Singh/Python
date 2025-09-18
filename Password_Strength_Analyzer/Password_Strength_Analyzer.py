# Write a Python program that:

# 1. Accepts a password from the user.
# 2. Checks for the following rules:
# - At least 8 characters long
# - Contains at least one uppercase letter
# - Contains at least one lowercase letter
# - Contains at least one digit
# - Contains at least one special character (!@#$%^&* etc.)

# 3. Assigns a strength level:
# - "Weak" if only 1–2 conditions are met
# - "Moderate" if 3–4 conditions are met
# - "Strong" if all 5 conditions are met

# 4. Prints a final message with suggestions (e.g., “Add more special characters to make your password stronger”).

# 5. 🎯 Example Runs
# - Enter password: hello123
# - Strength: Moderate
# - Suggestion: Add uppercase letters and special characters

import string
import time
import getpass

password=getpass.getpass("Enter Password : ")
is_len=1 if len(password)>=8 else 0
is_upper=1 if any(ch.isupper() for ch in password) else 0
is_lower=1 if any(ch.islower() for ch in password) else 0
is_digit=1 if any(ch.isdigit() for ch in password) else 0
is_punctuation=1 if any(ch in string.punctuation for ch in password) else 0

strength_counter=is_len+is_upper+is_lower+is_digit+is_punctuation

def suggestion(func):
    def wrapper(num):
        result=func(num)
        target=[is_len,is_upper,is_lower,is_digit,is_punctuation]
        wording=["words","uppercase","lowercase","numbers","special chars"]
        failed_req=[ch for (ch,w) in zip(wording,target) if w==0]
        if len(failed_req)>=2:
            suggested_text = "Add more " + ", ".join(failed_req[:-1]) + " and " + failed_req[-1] + "."            
        elif len(failed_req)==1:
            suggested_text="Add " + failed_req[0] + "."
        else:
            suggested_text=""        
        return f"{result}\n{suggested_text}"
    return wrapper

@suggestion
def strength_analyzer(strength_counter):    
    print("🔑 Checking password...")
    time.sleep(1)
    print("__"*30)
    print(f"Your Password : {password}")
    match strength_counter:
        case strength_counter if strength_counter<3:
            return f"Strength : Weak"
        case strength_counter if strength_counter<5:
            return f"Strength : Moderate"
        case _ :
            return f"Strength: Strong\nGood job! ✅"

print(strength_analyzer(strength_counter))