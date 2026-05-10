from functools import partial, reduce, lru_cache
from datetime import datetime

def multiply(a, b):
    return a * b

def Sum(data: list[int]):
    return reduce(lambda x, y: x + y, data)

def fibonacci(m):
    if m == 0:
        return 0
    elif m == 1:
        return 1
    else:
        return fibonacci(m - 1) + fibonacci(m - 2)

@lru_cache(maxsize=128, typed=False)
def fibonacci_lru(m):
    if m == 0:
        return 0
    elif m == 1:
        return 1
    else:
        return fibonacci_lru(m - 1) + fibonacci_lru(m - 2)


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7]
    func1 = partial(multiply, a=1, b=3); print(func1())
    func2 = partial(multiply, b=2); print(func2(10))
    
    func3 = Sum(data); print(func3)
    
    print("\nTesting Fibonacci Without lru_cache ...",)
    start = datetime.now()
    fibonacci(25)
    end = datetime.now()
    print(f"Execution time: {end - start}")

    print("\nTesting Fibonacci With lru_cache ...",)
    start = datetime.now()
    fibonacci_lru(25)
    end = datetime.now()
    print(f"Execution time: {end - start}")
