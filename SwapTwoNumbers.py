# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 14:22:21 2023

@author: kalypatn
"""

#swapping Two Numbers

x = int(input("Enter a value of X: "))
y = int(input("Enter a value of Y: "))

print(f"Before Swapping \n x = {x}, y = {y}")

#taking a temp variable

temp = x
x = y
y = temp

print(f"After Swapping \n x = {x}, y = {y}")