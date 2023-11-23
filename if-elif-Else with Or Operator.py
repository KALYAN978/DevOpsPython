# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 10:18:10 2023

@author: kalypatn
"""

gen = input("Enter your gender(M/F/T): ")

if gen == 'M' or gen == 'F':
    print("Your allowed")
elif gen == 'T':
     print("Sorry You are not allowed")
else:
    print("Animals are not allowed")