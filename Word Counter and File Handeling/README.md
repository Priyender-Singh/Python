# Python Word Counter

A simple Python project that:
- Accepts a paragraph of text from the user.
- Removes punctuation and converts words to lowercase.
- Counts how many times each word appears.
- Saves the results into a formatted file inside a uniquely named folder.
- Wraps the original paragraph neatly to a fixed width for readability.

---

## 📂 How It Works
1. The script asks the user for a folder path.
2. It automatically creates a new folder with a unique name like: `1_Word_Counter_2025_09_15`
3. Inside that folder, it saves a file named `Word_Count.txt`.
4. The file contains:
- The original paragraph (wrapped to 80 characters per line).
- A clean table of words and their counts.

---

## 🧑‍💻 Example

### Input
`Python is powerful, and Python is fun! Fun and powerful languages are loved by developers.`

### Output in `Word_Count.txt`

Python is powerful, and Python is fun! Fun and powerful languages are loved by 
developers.

Below are the words and their repetation from above paragraph

Words      Counts
Python     2
Is         2
Powerful   2
And        2
Fun        2
Languages  1
Are        1
Loved      1
By         1
Developers 1
