# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 12:55:59 2023

@author: kalypatn
"""

Locations = ["Bangalore","Hyderabad","Mumbai","Chennai","Pune"]
print("location order before 2023: \n")
print(Locations,"\n")

Locations.sort()
print("sorting locations list in increasing order: ")
print(Locations,"\n")


Locations.sort(reverse = True)
print("sorting locations list in decreasing order: ")
print(Locations)
