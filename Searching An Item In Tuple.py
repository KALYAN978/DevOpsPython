# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 14:47:40 2023

@author: kalypatn
"""

tuple = ("c","C++","Java","Python",1,2.7)
print(tuple)

search = input("Enter an Item to be Searched: ")

if search in tuple:
    print("Yes",search," is in the tuple")
else:
    print("No",search, " is not in the tuple")