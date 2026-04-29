def alternating_case(text: str) -> str:
    index = 0
    result = ""

    for c in text:
        if c.isalpha():
            result += c.upper() if index % 2 == 0 else c.lower()
            index += 1
        else:
            result += c
    return result
