# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 15:14:56 2023

@author: kalypatn
"""

a = int(input("Enter the first No:"))
b = int(input("Enter a second No:"))

if (a>b):
    min = a
else:
    min = b
    
while (1):
    if(min % a == 0 and min % b == 0):
        print("lcm is: " + min)
        break
    min = min + 1