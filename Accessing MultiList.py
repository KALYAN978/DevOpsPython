# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 14:18:46 2023

@author: kalypatn
"""

myList = [[1,2,3,4,5],[2,3,4,5,6,4,6,7],[3,6,9,12,15]]
print(myList)

for i in range(len(myList)):
    for j in range(len(myList[i])):
        print(myList[i][j], end=" ")
    print()