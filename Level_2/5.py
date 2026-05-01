def is_prime(n):
    p = 2
    while (p < n):
        if n % p == 0:
            return False
        p += 1
    return True

n = 2
while (n <= 100):
    if is_prime(n):
        print(n)
    n += 1