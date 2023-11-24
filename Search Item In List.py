# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 12:44:20 2023

@author: kalypatn
"""

Locations = ["Bangalore","Hyderabad","Mumbai","Chennai","Pune"]
print("location order before 2023: \n")
print(Locations,"\n")

search = input("Enter Your Location: ")

if search in Locations:
    print("Yes",search," is in the List")
else:
    print("No ,",search, " is not in the list")