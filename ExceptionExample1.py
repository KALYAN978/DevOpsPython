# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 22:23:11 2023

@author: kalypatn
"""

#exception example

try:
    x = int(input('Enter a  number: '))
    y = 10/x
    print(y)
except ZeroDivisionError:
    print("Division error")
except ValueError:
    print("Error: invalid input")