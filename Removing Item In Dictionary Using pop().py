# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 12:58:13 2023

@author: kalypatn
"""

bike = {"brand":"Bajaj",
        "Model":"Avenger",
        "year":2019,
        "engine":"220cc"}

for x in bike.items():
    print(x)
    
bike.pop("engine")

print("\nModified")
for x in bike.items():
    print(x)