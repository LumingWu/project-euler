#!/bin/python3

import sys

"""
This problem can be viewed as a dynamic programming problem where we
would like to map computed solution for future usage.
Again, here is a study for Fibonacci numbers
f(1) = 1
f(2) = 2
f(n) = f(n-1) + f(n-2)
"""
fibs = [1, 2]

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    while fibs[-1] < n:
        fibs.append(fibs[-1] + fibs[-2])
    index = 1
    sum = 0
    while index < len(fibs):
        if fibs[index] >= n:
            break
        sum += fibs[index]
        index += 3
    print(sum)
