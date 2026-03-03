class DivisionByZeroError(ValueError):
    """Raised when attempting to divide by zero."""
    pass


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise DivisionByZeroError("Cannot divide by zero.")
        return a / b

    def clear(self):
        return 0.0