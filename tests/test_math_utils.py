import pytest
from src.math_utils import add, subtract, multiply, divide


def test_add():
    assert add(3, 2) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(3, 2) == 1
    assert subtract(2, 3) == -1
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(3, 2) == 6
    assert multiply(0, 5) == 0
    assert multiply(-1, 2) == -2

def test_divide():
    assert divide(6, 2) == 3
    assert divide(5, 2) == 2.5
    with pytest.raises(ValueError):
        divide(3, 0)  # Should raise ValueError for division by zero