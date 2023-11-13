# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 15:33:06 2023

@author: kalypatn
"""

set = {1,2,"setting",4.5,'A',"B",'C'}
print(set)

set2 = {2,3,4,5,5,6,6,7}

set.update(set2)
print(set)