# SWE Testing Assignment

## 1. Project Overview

This project implements a simple calculator application ("Quick-Calc") developed as part of the Advanced Software Engineering course.

The main objective of this assignment is to demonstrate:

- Clean project structure  
- Proper use of version control (Git & GitHub)  
- Implementation of unit and integration tests  
- Edge case handling  
- Application of software testing principles  
- Release management using semantic versioning  

The calculator supports the four basic arithmetic operations and includes automated test coverage using the pytest framework.

---

## 2. Application Features

The calculator supports:

- Addition  
- Subtraction  
- Multiplication  
- Division  
- Graceful handling of division by zero  
- Clear (C) functionality to reset the result  

The focus of this project is not on UI complexity but on correctness, test quality, and code maintainability.

---

## 3. Project Structure

```
swe-testing-assignment/
│
├── src/                # Application source code
├── tests/              # Unit and integration tests
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation
└── TESTING.md          # Testing strategy documentation
```

---

## 4. Setup Instructions

### 4.1 Clone the Repository

```
git clone https://github.com/your-username/swe-testing-assignment.git
cd swe-testing-assignment
```

### 4.2 Create Virtual Environment (Recommended)

```
python -m venv venv
```

Activate:

Windows:
```
venv\Scripts\activate
```

macOS / Linux:
```
source venv/bin/activate
```

### 4.3 Install Dependencies

```
pip install -r requirements.txt
```

---

## 5. Running the Tests

To execute all unit and integration tests:

```
pytest
```

All tests should pass successfully before creating a release.

---

## 6. Testing Strategy Overview

This project follows a multi-layered testing approach aligned with the Testing Pyramid:

- A larger number of unit tests verify calculation logic in isolation.  
- A smaller set of integration tests validate interaction between components.  
- Edge cases such as division by zero and negative numbers are included.  

Detailed explanations are provided in TESTING.md.

---

## 7. Testing Framework Comparison

Two common Python testing frameworks are unittest and pytest.

Unittest:
- Built into Python standard library  
- Object-oriented structure  
- More verbose and requires boilerplate code  

Pytest:
- Cleaner and more readable syntax  
- Powerful assertion introspection  
- Flexible fixture system  
- Minimal boilerplate  
- Widely used in modern Python projects  

For this assignment, pytest was selected due to its simplicity, readability, and strong ecosystem support. It enables writing concise tests while maintaining clarity and maintainability.

---

## 8. Versioning & Release

The project follows Semantic Versioning.

Current stable release:

v1.0.0

This release represents a fully working calculator application with complete test coverage and documentation.

---

## 9. Author

Emir Dabagh  
Advanced Software Engineering  
Riga Technical University
