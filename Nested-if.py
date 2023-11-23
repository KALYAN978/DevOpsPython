# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 10:46:16 2023

@author: kalypatn
"""

n = int(input("Enter a number: "))

if n>10:
    print("Number is greater than to 10")
    if n%2 == 0:
        print("NUmber is even")
    else:
        print("Number is Odd")
else:
    print("Number is smaller than or equal to 10")