clean_text = ""
user_text = input("Enter a text: ")

for c in user_text:
    if c.isalpha():
        clean_text += c

if clean_text.lower() == clean_text[::-1].lower():
    print("String is palindrome!")
else:
    print("String is not palindrome!")
