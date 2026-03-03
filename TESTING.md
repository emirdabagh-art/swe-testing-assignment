# Testing Strategy

## Framework Selection
Pytest was chosen due to its simplicity, readability, and powerful fixture system.

## Test Types Implemented

### 1. Unit Tests
Each calculator method (add, subtract, multiply, divide) is tested independently.

### 2. Integration Tests
Simulated real user interaction flows combining multiple operations.

### 3. Edge Case Testing
- Division by zero
- Negative numbers
- Floating point inputs

## Execution

Run tests with:

```bash
py -m pytest
```

All tests pass successfully (15/15).
