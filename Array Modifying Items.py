# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 13:07:33 2023

@author: kalypatn
"""

import array as arr

numArr = arr.array('i',[10,20,30,40,50,60])

print("Array Items: ")
print(numArr)

numArr[3] = 100

print("\n Modified ")

print(numArr)

#changing 1st to 5th index values
numArr[1:5] = arr.array('i',[-8,-5,-6,-7])

print("\nrange has modified")
print(numArr)
