# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 13:44:10 2023

@author: kalypatn
"""

import array as arr

numArr = arr.array('i',[10,20,30,40,50,60])

print("Array Items: ")
print(numArr)

# add 25 at index 2
numArr.insert(2, 25)

print(numArr)