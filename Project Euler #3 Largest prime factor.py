#!/bin/python3

import sys

"""
http://thetaoishere.blogspot.com/2009/04/finding-largest-prime-factor.html
After 2 and 3, 6*n+1 or 6*n-1
After 5 is just 2 and 4 alternative. 5, 7, 11, 13, 17, 19 ...
For every factor, we keep dividing it until we can't.
The last remaining factor or n, which ever is larger, is the largest prime factor
"""

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    while not (n % 2):
        n = int(n // 2)
    if n == 1:
        print(2)
    else:
        while not (n % 3):
            n = int(n // 3)
        if n == 1:
            print(3)
        else:
            while not (n % 5):
                n = int(n // 5)
            if n == 1:
                print(5)
            else:
                factor = 7
                add_four = True
                square_root = int(n ** 0.5)
                while factor <= square_root:
                    while not (n % factor):
                        n = int(n / factor)
                    if add_four:
                        factor += 4
                        add_four = False
                    else:
                        factor += 2
                        add_four = True
                    square_root = int(n ** 0.5)
                if factor > n:
                    print(factor)
                else:
                    print(n)
