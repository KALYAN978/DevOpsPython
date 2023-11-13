# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 15:58:09 2023

@author: kalypatn
"""

import array as arr

numArr = arr.array('i',[10,20,30,40,50,60,70])

print(numArr)

numArr.insert(2, 25)
print(numArr)