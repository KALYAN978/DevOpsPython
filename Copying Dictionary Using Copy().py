# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 13:04:04 2023

@author: kalypatn
"""

bike = {"brand":"Bajaj",
        "Model":"Avenger",
        "year":2019,
        "engine":"220cc"}

for x in bike.items():
    print(x)
    
car = bike.copy()

print("\n Car Dictionary Data")
print(car)