def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a: float, b: float) -> float:
    """Returns the quotient of a divided by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")  # ✅ Explicitly raise ValueError
    return a / b