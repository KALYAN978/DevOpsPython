# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 12:55:26 2023

@author: kalypatn
"""

bike = {"brand":"Bajaj",
        "Model":"Avenger",
        "year":2019,
        "engine":"220cc"}

for x in bike.items():
    print(x)
    
search = input("Enter the key to be searched: ")

if search in bike:
    print("yes",search," is in bike")
else:
    print("No",search," is not in bike")