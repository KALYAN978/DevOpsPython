# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 15:10:25 2023

@author: kalypatn
"""

set = {1,2,"setting",4.5,'A',"B",'C'}
print(set)

search = input("Enter item to be searched: ")

if search in set:
    print("yes",search," is in the set")
else:
    print("No",search," is not in the set")