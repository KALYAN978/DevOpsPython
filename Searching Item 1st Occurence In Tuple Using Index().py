# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 14:50:43 2023

@author: kalypatn
"""

tuple = ("c","C++","Java","Python",1,2.7)
print(tuple)

course = input("Enter an Item to be searched: ")

x = tuple.index(course)
print("First Occurence of the ",course," is at index : ",x)