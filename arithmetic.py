# =========================================================
#  Project: Python Arithmetic Operations
#  Author: Ravina Sonawane
#  Description: Basic arithmetic functions with automated tests
# =========================================================


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the division of a by b. Raises ValueError on zero division."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


def modulus(a, b):
    """Return the remainder of a divided by b."""
    if b == 0:
        raise ValueError("Cannot perform modulus with zero!")
    return a % b


def power(a, b):
    """Return a raised to the power of b."""
    return a ** b


if __name__ == "__main__":
    print("=" * 45)
    print("   PYTHON ARITHMETIC OPERATIONS")
    print("=" * 45)

    num1 = 10
    num2 = 5

    print(f"Numbers: a = {num1}, b = {num2}\n")
    print(f"Addition ({num1} + {num2})       : {add(num1, num2)}")
    print(f"Subtraction ({num1} - {num2})    : {subtract(num1, num2)}")
    print(f"Multiplication ({num1} * {num2}) : {multiply(num1, num2)}")
    print(f"Division ({num1} / {num2})       : {divide(num1, num2)}")
    print(f"Modulus ({num1} % {num2})        : {modulus(num1, num2)}")
    print(f"Power ({num1} ** {num2})          : {power(num1, num2)}")
    print("=" * 45)
