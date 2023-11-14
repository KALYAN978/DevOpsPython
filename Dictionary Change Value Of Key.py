# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 12:44:45 2023

@author: kalypatn
"""

bike = {"brand":"Bajaj",
        "Model":"Avenger",
        "year":2019,
        "engine":"220cc"}

for x in bike.items():
    print(x)
    
bike["Model"] = "Pulsar"

print("\n Bike Details: ")
for x in bike.items():
    print(x)