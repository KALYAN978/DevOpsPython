# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 15:06:39 2023

@author: kalypatn
"""

def fact(n):
    if n <= 1:
        return 1
    else:
        n = n * fact(n-1)
        return n
    

n = int(input("Enter a number"))
print("Factorial of", n , fact(n))