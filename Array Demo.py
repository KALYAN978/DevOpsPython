# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 15:45:09 2023

@author: kalypatn
"""

import array

arrInt = array.array('i',[1,2,3,4,5])

arrFloat = array.array('f',[1.1,2.2,3.3,4.4])

arrChar = array.array('u',['A','B'])

print("IntegerArray")
for x in range(len(arrInt)):
    print(arrInt[x])

print("\nFloat Array: ")
for x in range(len(arrFloat)):
    print("{0:.2f}".format(arrFloat[x]))


print("\nChar Array")
for x in range(len(arrChar)):
    print(arrChar[x])
