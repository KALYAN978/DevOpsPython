# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 15:08:37 2023

@author: kalypatn
"""
#functions in list


list =  ["1",2,8.0,"4"]
print(list)

list.append("werewr")
print(list)


listA = list.copy()
print(listA)

listB = [1,2,3,4,5,6,7,8,9]

listC = listA + listB
print(listC)


listC.reverse()
print(listC)