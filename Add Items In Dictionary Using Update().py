# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 12:50:38 2023

@author: kalypatn
"""

bike = {"brand":"Bajaj",
        "Model":"Avenger",
        "year":2019,
        "engine":"220cc"}

for x in bike.items():
    print(x)
    
bike.update({"color":"Green"})

print(" \n Modified")
for x in bike.items():
    print(x)