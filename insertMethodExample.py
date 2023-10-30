# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 14:33:14 2023

@author: kalypatn
"""

#insert method

list = [1,2,3,4,5,6,7,8]
print(list)

newNumber = list.insert(3, 3)
print(list)

n = int(input("enter a number: "))

index = int(input("enter an index number: "))

list.insert(index,n)
print(list)