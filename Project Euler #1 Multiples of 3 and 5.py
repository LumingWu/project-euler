#!/bin/python3

import sys

"""
This is a arithmetic series
Where the equation is 1 + 2 + 3 ... n = n * ( n + 1) / 2
We get fifteens to minus the duplicates.
"""

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    threes = int((n - 1) // 3)
    fives = int((n - 1) // 5)
    fifteens = int((n - 1) // 15)
    print(int((3 * threes * (threes + 1) + 5 * fives * (fives + 1) - 15 * fifteens * (fifteens + 1)) // 2))
