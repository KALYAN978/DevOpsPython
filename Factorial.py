# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 13:24:11 2023

@author: kalypatn
"""

#4! = 4*3*2*1

fact = 1
n = int(input("Enter a Number: "))

for i in range(1,n+1):  #in Range --> n+1 will go to n value only
    fact = fact * i
print(f"Factorial of {n} is: {fact}")