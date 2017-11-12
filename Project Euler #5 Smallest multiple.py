#!/bin/python3

import sys

"""
A simple Wiki will tell us to do LCM(Largest Common Multiple) with
A*B / GCD(Greatest Common Factor)
"""

#Euclidean Algorithm
def gcd(A, B):
    while True:
        if A < B:
            C = A
            A = B
            B = C
        R = A % B
        if R == 0:
            return B
        A = B
        B = R

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    result = 1
    for i in range(2, n + 1):
        result = int(result * i // gcd(result, i))
    print(result)
