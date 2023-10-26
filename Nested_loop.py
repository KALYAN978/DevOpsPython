# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 09:46:45 2023

@author: kalypatn
"""

i = 1
j = 0

while i<=5:
    
    while j<i:
        print("*", end = "")
        j=j+1
        
    i = i+1
    j = 0
    print("")