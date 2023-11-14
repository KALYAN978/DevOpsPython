# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 14:37:11 2023

@author: kalypatn
"""

x = 100

def fun():
    global x
    y=20
    x = 50
    print("value of y", y)
    

print("Value of X: ",x)

fun()

print("Value of X (after func call): ",x)

fun()