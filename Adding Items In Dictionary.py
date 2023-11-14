# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 12:48:22 2023

@author: kalypatn
"""

bike = {"brand":"Bajaj",
        "Model":"Avenger",
        "year":2019,
        "engine":"220cc"}

for x in bike.items():
    print(x)
    
bike["color"] = "Green"

print("\nModified")
for x in bike.items():
    print(x)