"""
string_utils.py - Provides basic string functions.
"""

def reverse_string(s):
    """Returning a reverse of given string."""
    return s[::-1]

def is_palindrome(s):
    """Checking to see if text is a palindrome."""
    processed_text = ''.join(filter(str.isalnum, s)).lower()
    return processed_text == processed_text[::-1]

def count_vowels(s):
    """Counting vowels in a given string."""
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in s:
        if char in vowels:
            vowel_count += 1
    return vowel_count
