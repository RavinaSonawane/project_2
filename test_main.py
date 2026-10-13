# ========================================
#  Tests for main.py functions
# ========================================

from main import greet, calculate_average, is_even
from main import save_student_info, read_student_info
import os


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


# --- Day 1: File Handling Tests (NEW!) ---

def test_save_student_info():
    """Test saving student info to a file."""
    test_student = {"name": "Test", "course": "Science", "year": 1}
    test_file = "test_student_temp.txt"

    # Save and check it returns True
    result = save_student_info(test_student, test_file)
    assert result == True

    # Check file actually exists
    assert os.path.exists(test_file)

    # Check file content
    with open(test_file, "r") as f:
        content = f.read()
    assert "name: Test" in content
    assert "course: Science" in content

    # Clean up — delete the test file
    os.remove(test_file)


def test_read_student_info():
    """Test reading student info from a file."""
    test_file = "test_read_temp.txt"

    # Create a test file first
    with open(test_file, "w") as f:
        f.write("name: Ravina\ncourse: CS\n")

    # Read it back
    content = read_student_info(test_file)
    assert content is not None
    assert "name: Ravina" in content
    assert "course: CS" in content

    # Clean up
    os.remove(test_file)


def test_read_missing_file():
    """Test reading a file that doesn't exist — should return None, not crash!"""
    result = read_student_info("this_file_does_not_exist.txt")
    assert result is None
