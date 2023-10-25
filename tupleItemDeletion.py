# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 14:57:44 2023

@author: kalypatn
"""

#tuple to list -> list to tuple

thistuple = ("apple","usjad","u")
y=list(thistuple)
y.remove("u")
thistuple=tuple(y)
print(y)
print(thistuple)