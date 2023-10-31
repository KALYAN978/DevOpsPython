# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 13:31:36 2023

@author: kalypatn
"""

def fact(n):
    if n <= 1:
        return 1
    else:
        n = n * fact(n-1)
        return n


n = int(input("Enter a number: "))
print(f"Factorial of {n} is: {fact(n)}")
