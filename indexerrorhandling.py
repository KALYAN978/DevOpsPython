# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 12:25:28 2023

@author: kalypatn
"""

#Indexerrorhandling

#converting formatted string to a list
fruits = eval(input())

def make_pie(index):
    try:
        fruit = fruits[index]
    except:
        print("Fruit pie")
    else:
        print(fruit + " pie")

make_pie(4)
    

