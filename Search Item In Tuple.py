# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 14:34:47 2023

@author: kalypatn
"""


tuple = ("c","C++","java","Python",1,2.0,'A','B')
print(tuple,"\n")


search = input("Enter Item to be searched: ")

if search in tuple:
    print("Yes", search, " is in tuple")
else:
    print("No", search," is not in tuple")