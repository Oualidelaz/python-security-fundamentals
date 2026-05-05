import string

letters = string.ascii_letters
text = "hello from python, I am oualid, how are you!"
for c in letters:
    if text.count(c) > 0:
        print(f"Character '{c}': {text.count(c)}")
