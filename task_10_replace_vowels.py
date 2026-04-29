def replace_vowels(text: str) -> str:
    for c in text:
        if c in "aieuo":
            text = text.replace(c, "*")
    return text
