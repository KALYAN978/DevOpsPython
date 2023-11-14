# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 12:59:46 2023

@author: kalypatn
"""

bike = {"brand":"Bajaj",
        "Model":"Avenger",
        "year":2019,
        "engine":"220cc"}

for x in bike.items():
    print(x)
    
del bike["engine"]
print("\n modified")

for x in bike.items():
    print(x)