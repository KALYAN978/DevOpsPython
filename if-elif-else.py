# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 10:14:27 2023

@author: kalypatn
"""

num = input("Enter a Number")

if int(num) == 0:
    print("Zero is entered")
elif int(num) < 0:
    print("Number cannot be negative")
else:
    print("You Have entered another number")