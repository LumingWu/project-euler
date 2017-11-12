#!/bin/python3

import sys

def hasFactor(palindrome):
    for i in range(999, 99, -1):
        # Will not get 3 digit, stop
        if palindrome / i > 999:
            break
        # Divisible and passed 3 digit test, return True
        if not(palindrome % i):
            return True
    return False

def to_six_digit_palindrome(three_digit):
    return three_digit * 1000 + int(three_digit % 100 % 10 * 100) + int(three_digit // 10 % 10 * 10) + int(three_digit // 100)
        
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    """
    Assume n is 800,010, the immediate six_digit_palindrome is 800,008.
    But 800,007 would not have 800,008 as immediate palindrome.
    So we decide that from start.
    """
    decrement = 1
    if to_six_digit_palindrome(int(n // 1000)) < n:
        decrement = 0
    for three_digit in range(int(n // 1000) - decrement, 99, -1):
        six_digit_palindrome = to_six_digit_palindrome(three_digit)
        if hasFactor(six_digit_palindrome):
            print(six_digit_palindrome)
            break
