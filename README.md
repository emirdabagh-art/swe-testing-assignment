# SWE Testing Assignment

## 1. Project Overview

This project implements a simple calculator application with full unit and integration test coverage using the pytest testing framework.

The purpose of this assignment is to demonstrate:
- Proper project structure
- Use of automated testing frameworks
- Unit and integration testing practices
- Edge case validation
- Version control and release management

---

## 2. Project Structure

```
swe-testing-assignment/
│
├── src/                # Application source code
├── tests/              # Unit and integration tests
├── requirements.txt    # Project dependencies
├── TESTING.md          # Testing strategy documentation
└── README.md           # Project documentation
```

---

## 3. Testing Framework Selection

Pytest was selected because:

- It is lightweight and easy to use
- It provides a powerful fixture system
- It allows clean and readable test syntax
- It is widely adopted in Python projects

---

## 4. Test Coverage

The following types of tests were implemented:

### 4.1 Unit Tests
Each calculator method (add, subtract, multiply, divide) is tested independently.

### 4.2 Integration Tests
Simulated real-world usage combining multiple operations.

### 4.3 Edge Case Testing
- Division by zero
- Negative number handling
- Floating-point input validation

All tests pass successfully (15/15).

---

## 5. Installation & Execution

Install dependencies:

```bash
py -m pip install -r requirements.txt
```

Run tests:

```bash
py -m pytest
```

---

## 6. Versioning

Current stable release: **v1.0.0**

The project follows semantic versioning.
