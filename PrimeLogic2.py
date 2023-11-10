# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 14:09:54 2023

@author: kalypatn
"""

#prime number logic 2

x = 2
ch = 0

n = int(input("Enter a no"))

if n <= 1:
    ch = 1
    
while x <= n/2:
    if n/x == 0:
        ch = 1
        break
    else:
        x += 1

if ch == 0:
    print("prime No")
else:
    print("not a prime")