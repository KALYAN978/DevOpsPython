# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 11:56:37 2023

@author: kalypatn
"""

#Lambda Function example

def commonFunction(value):
    return lambda a : a * value

DoubleIt = commonFunction(2)
TripleIt = commonFunction(3)

print(DoubleIt)
print(commonFunction(3))