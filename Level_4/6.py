import random

def mac_generator():
    n = [random.choice("0123456789ABCDEF") for _ in range(11)]
    second_n = random.choice("02468ACE")
    n.insert(1, second_n)
    mac = ':'.join(''.join(n[i:i+2]) for i in range(0, 12, 2))
    return mac
