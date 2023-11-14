# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 13:01:33 2023

@author: kalypatn
"""

bike = {"brand":"Bajaj",
        "Model":"Avenger",
        "year":2019,
        "engine":"220cc"}

for x in bike.items():
    print(x)
    

bike.clear()

for x in bike.items():
    print(x)

print("Items Deleted")