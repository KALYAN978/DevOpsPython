# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 12:35:51 2023

@author: kalypatn
"""

for x in range(1,11):
    for y in range(1,11):
        print("{0:02d} ".format(x*y), end="")
    print();