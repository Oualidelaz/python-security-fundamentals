from collections.abc import Callable
import random

def Attack1(target: str, power: int) -> str:
    return f"Firewall blocks {target} for {power} units"

def Action(target: str, power: int):
    return f"Patch applied to {target} restoring {power} units"

def make_counter(func1: Callable, func2: Callable):
    counter = 0
    # Nested Function (Closure)
    def increment():
        # nonlocal
        nonlocal counter
        f1 = func1("192.168.1.1", 50); print(f1)
        counter += random.randint(0, 100); print(f"Counter {counter}")
        f2 = func2("database_server", 30); print(f2)
    return increment

if __name__ == "__main__":
    # First-Class Functions
    counter = make_counter(Attack1, Action)
    counter()
