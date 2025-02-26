import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.string_utils import reverse_string, is_palindrome, count_vowels

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("") == ""

def test_is_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("A man, a plan, a canal, Panama") == True  # Ignores spaces and punctuation

def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("PYTHON") == 1
    assert count_vowels("aeiouAEIOU") == 10
    assert count_vowels("bcdfg") == 0