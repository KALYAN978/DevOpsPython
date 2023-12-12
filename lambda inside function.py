# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 13:59:28 2023

@author: kalypatn
"""

def double(n):
    return lambda a:a * n

cal = double(2)
print("Result: ",cal(4))


