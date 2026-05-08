import string

def password(pswrd):
    try:
        specials = string.punctuation
        if len(pswrd) >= 8:
            if any(char.isdigit() for char in pswrd):
                if any(True for char in pswrd if char in specials):
                    return (f"Password: '{pswrd}' is strong!")
                else:
                    raise ValueError("Password should contains special character")            
            else:
                raise ValueError("Password should contains digits")            
        else:
            raise ValueError("Password length should be >= 8")
    except Exception as e:
        return e

