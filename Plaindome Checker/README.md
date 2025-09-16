## Palindrome Checker

- This project contains two Python scripts for working with palindromes.
- A palindrome is a word, phrase, or sequence that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

# 📌 Code A – Word/Sentence Palindrome Checker

`This script checks if the entire input (word or sentence) is a palindrome.`

**Features**

1. Accepts a word or sentence.
2. Ignores spaces, punctuation, and capitalization.
3. Prints Palindrome ✅ if true, otherwise Not a Palindrome ❌.

**Example**
`Input: Madam, in Eden, I’m Adam`
`Output: Palindrome ✅`

**Code Snippet**
`Plaindrom word and sentences`

## 📌 Code B – Palindromic Word Finder

`This script finds palindromic words within a sentence.`

**Features**

1. Accepts a sentence from the user.
2. Removes punctuation and converts to lowercase.
3. Splits sentence into words.
4. Detects palindromic words.
5. Displays:
- Palindromic words.
- Palindromic word count.
- Non-palindromic word count.
- The longest palindrome word.

**Example**
`Input: Madam Arora teaches malayalam. Did Hannah see bees? Eve!`
**Output:**
`Palindromic words : ['madam', 'arora', 'malayalam', 'did', 'hannah', 'eve']`
`Palindromic words count: 6`
`Non-palindromic words count: 3`
`Longest palindrome: malayalam`

**Code Snippet**
`Plaindrom word counter`

# ⚡ How to Run

1. Save the scripts as **Code A** `Plaindrom word and sentences.py` and **Code B** `Plaindrom word counter.py`.
- `python code_a.py   # For sentence/word palindrome check`
- `python code_b.py   # For word-level palindrome finder`
2. Run them in the terminal with Python 3:

# 📚 Concepts Used

- String methods (.lower(), .strip(), .isalnum()).
- List comprehensions.
- Conditional expressions (x if condition else y).
- Built-in functions like max() with key=len.
- The string module for handling punctuation.

