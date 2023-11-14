# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 14:30:41 2023

@author: kalypatn
"""

# 4! = 4 * 3 * 2 * 1
#Factorial of O is 1

def fact(n):
    if n <= 1:
        return 1
    else:
        n = n * fact(n-1)
        return n
    
n = int(input("Enter a Number: "))
print("Factorial of ",n, " is ", fact(n))