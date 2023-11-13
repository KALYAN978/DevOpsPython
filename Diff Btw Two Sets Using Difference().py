# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 15:37:58 2023

@author: kalypatn
"""

set = {1,2,"setting",4.5,'A',"B",'C'}
print(set)

laptops = {"dell", "hp","lenovo"}

onlyLaptops = laptops.difference(set)
print(laptops)
print(set)
print(onlyLaptops)