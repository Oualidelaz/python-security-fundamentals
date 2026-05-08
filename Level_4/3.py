import string
import random

def password_generator():
    letters_s = string.ascii_lowercase
    letters_c = string.ascii_uppercase
    specials = string.punctuation
    numbers = string.digits

    l_s = random.choices(letters_s, k=3)
    l_c = random.choices(letters_c, k=3)
    s = random.choices(specials, k=3)
    n = random.choices(numbers, k=3)

    combine = l_s + l_c + s + n
    random.shuffle(combine)
    print("".join(combine))

password_generator()