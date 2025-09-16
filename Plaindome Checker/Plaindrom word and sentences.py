
word=input("Enter word/sentence :\n").strip()
word="".join(ch.lower() for ch in word if ch.isalnum())

print("Palindrome ✅") if word==word[::-1] else print("Not a Palindrome ❌")