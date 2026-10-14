# 🐍 Python Learning & CI/CD Portfolio
Author: **Ravina Sonawane**

A hands-on Python repository demonstrating clean code architecture, SQLite database integration, automated unit testing with `pytest`, and continuous integration (CI) with **GitHub Actions**.

---

## 📁 Projects in This Repository

### 1. 💰 Personal Expense & Budget Tracker (`expense_tracker.py`)
A lightweight, robust command-line application backed by **SQLite** to manage personal finances and track category-wise spending.

#### Features:
- **SQLite Database Persistence:** Stores transactions with `id`, `title`, `amount`, `category`, and `date`.
- **Data Validation:** Rejects negative/zero amounts and empty titles/categories.
- **Spending Analytics:**
  - Calculate total expenditures.
  - Category breakdown with percentages and visual ASCII progress bars.
- **CRUD Operations:** Add expenses, list all records, filter by category, and delete records by ID.
- **Automated Unit Tests:** 8 isolated tests in `test_expense_tracker.py` using pytest fixtures.

---

### 2. 🔢 Arithmetic Operations (`arithmetic.py`)
A fundamental Python module implementing core mathematical operations (`add`, `subtract`, `multiply`, `divide`, `modulus`, `power`) with edge-case validation (divide-by-zero protection). Tested with 8 unit tests in `test_arithmetic.py`.

---

### 3. 🎓 Python Fundamentals Demo (`main.py`)
Demonstration of Python variables, lists, dictionaries, functions, and file I/O (`student.txt`). Tested in `test_main.py`.

---

## 🚀 How to Run Locally

### Run the Programs
```bash
# Run Expense & Budget Tracker
python3 expense_tracker.py

# Run Arithmetic Operations
python3 arithmetic.py

# Run Python Basics Demo
python3 main.py
```

### Run All Unit Tests
```bash
pytest -v
```

To run tests for a specific module:
```bash
pytest test_expense_tracker.py -v
pytest test_arithmetic.py -v
pytest test_main.py -v
```

---

## 🔄 CI/CD Pipeline (`.github/workflows/ci.yml`)

This repository is connected to **GitHub Actions**:
- **Triggers:** Every `git push` or `pull_request` to the `main` branch.
- **Environment:** Ubuntu with Python 3.12.
- **Automated Steps:**
  1. Clones repository code.
  2. Sets up Python 3.12 and installs dependencies (`pytest`).
  3. Executes application smoke tests (`python arithmetic.py`, `python expense_tracker.py`, `python main.py`).
  4. Runs all 22 automated tests via `pytest -v`.
  5. Validates build integrity with green checkmark `✅`.

---

## 👤 Author
**Ravina Sonawane**
