import random
import string

text = "Hello"
length = len(text)

for i in range(length):
    print(text[:i])
    print(text[:i + 1])


