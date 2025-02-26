def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    processed_text = ''.join(filter(str.isalnum, s)).lower()
    return processed_text == processed_text[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in s:
        if char in vowels:
            vowel_count += 1
    return vowel_count
