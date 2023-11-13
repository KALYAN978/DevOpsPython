# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 15:53:27 2023

@author: kalypatn
"""

import array as arr

numArr = arr.array('i',[10,20,30,40,50,60,70])

print(numArr[3:6]) # 4th to 6th

print(numArr[:-3]) # beginning to 5th

print(numArr[3:])  # 4th to end

print(numArr[:])  # beginning to end
