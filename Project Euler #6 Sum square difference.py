#!/bin/python3

import sys

"""
For square of sum, we can use arithmetic series
From sum of squares, we see that 1 + 4 + 9 + 16 + 25...
1 + 3 = 4
4 + 5 = 9
9 + 7 = 16
16 + 9 = 25
(0 + 1) + (0 + 1 + 3) + (0 + 1 + 3 + 5)
Basically still arithmetic series but check out sum of first k perfect squares
(n * (n + 1) / 2) * (2n + 1) / 3
"""

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    square_of_sum = int((n * (n + 1) // 2) ** 2)
    # For N = 1
    sum_of_squares = int((n * (n + 1) // 2) * (2 * n + 1) // 3)
    print(square_of_sum - sum_of_squares)
