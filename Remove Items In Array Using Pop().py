# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 13:51:55 2023

@author: kalypatn
"""

import array as arr

numArr = arr.array('i',[10,20,30,30,40])

print(numArr)

#deleting item at index 3
numArr.pop(3)
print(numArr)