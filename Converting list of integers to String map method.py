# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 14:25:15 2023

@author: kalypatn
"""

# Creating a list with some elements of int data type  
iterable = ["Python", "Convert", 11, "List", 12, "String", "Method"]  

string = " ".join (map (str, iterable))
#map() method --> convert the integer elements into a string before converting the whole list to a string  

print (string)  
print (type(string)) 