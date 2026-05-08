def extract_vowels(text):
    result = ""
    for c in text:
        if c.lower() in "eiuao":
            result += c
    return result
