import pytest

from src.calculator import Calculator, DivisionByZeroError


@pytest.fixture()
def calc():
    return Calculator()


def test_add_two_integers(calc):
    assert calc.add(5, 3) == 8


def test_add_with_negative(calc):
    assert calc.add(-5, 3) == -2


def test_subtract_basic(calc):
    assert calc.subtract(10, 4) == 6


def test_subtract_result_negative(calc):
    assert calc.subtract(4, 10) == -6


def test_multiply_basic(calc):
    assert calc.multiply(6, 7) == 42


def test_multiply_with_decimal(calc):
    assert calc.multiply(2.5, 2) == 5.0


def test_divide_basic(calc):
    assert calc.divide(8, 2) == 4


def test_divide_decimal_result(calc):
    assert calc.divide(5, 2) == 2.5


def test_divide_by_zero_raises(calc):
    with pytest.raises(DivisionByZeroError):
        calc.divide(10, 0)


def test_large_numbers(calc):
    assert calc.add(10**12, 10**12) == 2 * 10**12


def test_clear_returns_zero(calc):
    assert calc.clear() == 0.0


def test_divide_negative_numbers(calc):
    assert calc.divide(-9, 3) == -3