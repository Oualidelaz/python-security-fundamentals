import hashlib

def md5_hash(text):
    result = hashlib.md5(text.encode())
    return result.hexdigest()
