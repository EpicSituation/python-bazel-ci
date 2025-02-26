"""
test_string_utils.py - testing basic string functions.
"""

import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.string_utils import reverse_string, is_palindrome, count_vowels

def test_reverse_string():
    """Testing reverse string function."""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("") == ""

def test_is_palindrome():
    """Testing is palindrone function."""
    assert is_palindrome("racecar") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("A man, a plan, a canal, Panama") is True  # Ignores spaces and punctuation

def test_count_vowels():
    """Testing count vowels function."""
    assert count_vowels("hello") == 2
    assert count_vowels("PYTHON") == 1
    assert count_vowels("aeiouAEIOU") == 10
    assert count_vowels("bcdfg") == 0
    