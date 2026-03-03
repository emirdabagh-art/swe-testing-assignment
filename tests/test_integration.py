import pytest

from src.calculator import Calculator, DivisionByZeroError


class QuickCalcSession:
    def __init__(self):
        self.calc = Calculator()
        self.display = 0
        self.pending_value = None
        self.pending_op = None

    def enter_number(self, value):
        self.display = value

    def press_op(self, op):
        self.pending_value = self.display
        self.pending_op = op

    def press_equals(self):
        if self.pending_op == "+":
            self.display = self.calc.add(self.pending_value, self.display)
        elif self.pending_op == "-":
            self.display = self.calc.subtract(self.pending_value, self.display)
        elif self.pending_op == "*":
            self.display = self.calc.multiply(self.pending_value, self.display)
        elif self.pending_op == "/":
            self.display = self.calc.divide(self.pending_value, self.display)
        return self.display

    def press_clear(self):
        self.display = self.calc.clear()
        return self.display


@pytest.fixture
def session():
    return QuickCalcSession()


def test_full_user_flow_addition(session):
    session.enter_number(5)
    session.press_op("+")
    session.enter_number(3)
    assert session.press_equals() == 8


def test_clear_resets_display(session):
    session.enter_number(99)
    assert session.press_clear() == 0.0


def test_division_by_zero_propagates(session):
    session.enter_number(10)
    session.press_op("/")
    session.enter_number(0)
    with pytest.raises(DivisionByZeroError):
        session.press_equals()