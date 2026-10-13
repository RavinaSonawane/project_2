# ========================================
#  Simple Python Program - Basics Demo
#  Author: Ravina Sonawane
# ========================================

# --- 1. Variables & Data Types ---
name = "Ravina"
age = 22
height = 5.5
is_student = True

print("=" * 40)
print("   PYTHON BASICS DEMO")
print("=" * 40)

print(f"\nName     : {name}")
print(f"Age      : {age}")
print(f"Height   : {height} ft")
print(f"Student  : {is_student}")


# --- 2. List Operations ---
colors = ["Red", "Blue", "Green", "Yellow", "Purple"]

print(f"\n--- Favorite Colors ({len(colors)} total) ---")
for i, color in enumerate(colors, 1):
    print(f"  {i}. {color}")


# --- 3. Dictionary ---
student = {
    "name": "Ravina",
    "course": "Computer Science",
    "year": 3,
    "grade": "A"
}

print("\n--- Student Info ---")
for key, value in student.items():
    print(f"  {key.capitalize():10}: {value}")


# --- 4. Functions ---
def greet(person_name):
    """Return a greeting message."""
    return f"Hello, {person_name}! Welcome to Python!"


def calculate_average(numbers):
    """Calculate and return the average of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0


# Using the functions
print(f"\n--- Functions Demo ---")
print(f"  {greet(name)}")

scores = [85, 92, 78, 95, 88]
avg = calculate_average(scores)
print(f"  Scores  : {scores}")
print(f"  Average : {avg:.1f}")

print(f"  Is 10 even? {is_even(10)}")
print(f"  Is 7 even?  {is_even(7)}")


# --- 5. Loop with condition ---
print("\n--- Even numbers from 1 to 10 ---")
even_numbers = [n for n in range(1, 11) if is_even(n)]
print(f"  {even_numbers}")



# --- 6. File Handling (Day 1 - NEW!) ---
def save_student_info(student_dict, filename="student.txt"):
    """Save student info to a text file.

    Args:
        student_dict: Dictionary with student data
        filename: Name of file to save to (default: student.txt)
    """
    try:
        with open(filename, "w") as file:
            for key, value in student_dict.items():
                file.write(f"{key}: {value}\n")
        print(f"\n  ✅ Student info saved to '{filename}'")
        return True
    except IOError:
        print(f"\n  ❌ Error: Could not write to '{filename}'")
        return False


def read_student_info(filename="student.txt"):
    """Read student info from a text file.

    Args:
        filename: Name of file to read from (default: student.txt)

    Returns:
        The file content as a string, or None if file not found
    """
    try:
        with open(filename, "r") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"\n  ❌ Error: File '{filename}' not found!")
        return None


# --- Using File Handling ---
print("\n--- File Handling Demo ---")

# Save the student dictionary to a file
save_student_info(student)

# Read it back
print("\n--- Reading from file ---")
content = read_student_info()
if content:
    print(content)

# Try reading a file that doesn't exist (error handling demo)
print("--- Error Handling Demo ---")
result = read_student_info("does_not_exist.txt")
if result is None:
    print("  (We handled the error — program didn't crash!)")


print("\n" + "=" * 40)
print("  ✅ Program completed successfully!")
print("=" * 40)
