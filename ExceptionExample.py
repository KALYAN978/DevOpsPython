# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 12:15:05 2023

@author: kalypatn
"""

#Exception example

height = input("Height: ")
weight = input("Weight: ")

if height > 3:
    raise ValueError("Human height should not be greater than 3 meters")

bmi = weight / height ** 2
print(bmi)

