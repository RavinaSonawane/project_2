# 🔢 Python_Arithmetic_Operation

A beginner-friendly Python project demonstrating fundamental arithmetic operations with automated unit testing and a GitHub Actions CI/CD pipeline.

---

## 📌 Features

- **Core Arithmetic Operations:**
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`*`)
  - Division with zero-division error handling (`/`)
  - Modulus (`%`)
  - Power / Exponentiation (`**`)
- **Automated Testing:** Unit tests written with `pytest` covering normal inputs and edge cases.
- **CI/CD Pipeline:** Automated GitHub Actions workflow triggers on every push and pull request to run tests and ensure code quality.

---

## 🚀 How to Run Locally

### 1. Run the Python Program
```bash
python arithmetic.py
```

### 2. Run the Unit Tests
```bash
pytest -v
```

Or run tests specifically for arithmetic operations:
```bash
pytest test_arithmetic.py -v
```

---

## 🔄 CI/CD Workflow (`.github/workflows/ci.yml`)

Every time code is pushed to the repository:
1. GitHub starts an Ubuntu virtual environment.
2. Checks out the code and sets up Python 3.12.
3. Installs dependencies (`requirements.txt`).
4. Executes `arithmetic.py` and `main.py`.
5. Runs all `pytest` unit tests.
6. Reports success (`✅`) or alerts you if any test fails.

---

## 👤 Author
Ravina Sonawane
