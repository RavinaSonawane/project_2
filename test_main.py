# ========================================
#  Tests for main.py functions
# ========================================

from main import greet, calculate_average, is_even


def test_greet():
    """Test the greet function."""
    assert greet("Ravina") == "Hello, Ravina! Welcome to Python!"
    assert greet("World") == "Hello, World! Welcome to Python!"


def test_calculate_average():
    """Test the calculate_average function."""
    assert calculate_average([10, 20, 30]) == 20.0
    assert calculate_average([100]) == 100.0
    assert calculate_average([]) == 0


def test_is_even():
    """Test the is_even function."""
    assert is_even(2) == True
    assert is_even(4) == True
    assert is_even(3) == False
    assert is_even(7) == False
    assert is_even(0) == True
