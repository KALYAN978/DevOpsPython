# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 14:31:17 2023

@author: kalypatn
"""

x = int(input("Enter a value of X: "))
y = int(input("Enter a value of Y: "))

print(f"Before Swapping \n x = {x}, y = {y}")

x = x + y
y = x - y
x = x - y


print(f"After Swapping \n x = {x}, y = {y}")