text = "Password"
for c in text:
    if c.lower() in "aieuo":
        text = text.replace(c, "*")
print(text)

