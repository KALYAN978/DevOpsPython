# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 14:27:59 2023

@author: kalypatn
"""

x = int(input("Enter a value of X: "))
y = int(input("Enter a value of Y: "))

print(f"Before Swapping \n x = {x}, y = {y}")

x,y = y,x
print(f"After Swapping \n x = {x}, y = {y}")