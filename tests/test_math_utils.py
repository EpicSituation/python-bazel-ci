"""
test_math_utils.py - testing basic mathematical functions.
"""

import pytest
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.math_utils import add, subtract, multiply, divide


def test_add():
    """Testing add function."""
    assert add(3, 2) == 5
    assert add(-1, 1) == 0

def test_subtract():
    """Testing subtract function."""
    assert subtract(3, 2) == 1
    assert subtract(2, 3) == -1
    assert subtract(0, 0) == 0

def test_multiply():
    """Testing multiply function."""
    assert multiply(3, 2) == 6
    assert multiply(0, 5) == 0
    assert multiply(-1, 2) == -2

def test_divide():
    """Testing Divide function."""
    assert divide(6, 2) == 3
    assert divide(5, 2) == 2.5
    with pytest.raises(ValueError):
        divide(3, 0)  # Should raise ValueError for division by zero
