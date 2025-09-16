
import string

word=input("Enter word/sentence :\n").strip()
new_word="".join(ch.lower() for ch in word if ch not in string.punctuation)
new_word=new_word.split(" ")
palindromes=[ch for ch in new_word if ch==ch[::-1]]

if len(palindromes) != 0:
    longest_palindromes=max(palindromes, key=len)
    print(f"Palindromic words : {palindromes}")
    print(f"Palindromic words count: {len(palindromes)}")
    print(f"Non-palindromic words count: {len(new_word)-len(palindromes)}")
    print(f"Longest palindrome: {longest_palindromes}")
else:
    print("**No palindrome word avaialble**")
