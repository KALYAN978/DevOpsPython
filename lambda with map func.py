# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 15:32:59 2023

@author: kalypatn
"""

def square(n):
    return n * n

result = map(square,[1,2,3,4,5])

print("Square of numbers in the list: ")
print(list(result))