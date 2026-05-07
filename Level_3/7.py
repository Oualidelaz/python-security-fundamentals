from nt import dup


data = [12, 232, 231, 231, 134, "Hello", 23, "Hello"]
n = len(data)
duplicates = []

for i in range(n):
    for j in range(n - i):
        print(i, "-> ", j)
