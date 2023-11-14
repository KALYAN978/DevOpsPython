# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 13:59:14 2023

@author: kalypatn
"""

import array as arr

numArr = arr.array('i',[10,342,43534,345342,23423])

print(numArr)

numArr2 = arr.array('i',["ksuhdf","bkuad","igyadsg"])

numArr.extend(numArr2)

print(numArr)