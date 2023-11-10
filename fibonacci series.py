# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 15:09:58 2023

@author: kalypatn
"""

a = 0
b = 1
n = input("Enter n for how many times for generate series")

print("FIBONACCI SERIES")
for i in range(n):
    c = a + b
    a = b
    b = c
    print(" ",c, end=" ")