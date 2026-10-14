# =========================================================
#  Tests for Python Arithmetic Operations
# =========================================================

import pytest
from arithmetic import add, subtract, multiply, divide, modulus, power


def test_add():
    assert add(10, 5) == 15
    assert add(-2, 2) == 0
    assert add(-5, -5) == -10
    assert add(2.5, 3.5) == 6.0


def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(5, 10) == -5
    assert subtract(-2, -3) == 1


def test_multiply():
    assert multiply(4, 5) == 20
    assert multiply(-3, 4) == -12
    assert multiply(0, 100) == 0


def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(9, 3) == 3.0
    assert divide(-10, 2) == -5.0


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(10, 0)


def test_modulus():
    assert modulus(10, 3) == 1
    assert modulus(10, 5) == 0


def test_modulus_by_zero():
    with pytest.raises(ValueError, match="Cannot perform modulus with zero!"):
        modulus(10, 0)


def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(4, 2) == 16
