# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 14:19:16 2023

@author: kalypatn
"""

def fun(*progLang):
    print("Programming Languages known: ")
    for x in progLang:
        print(x)
        

print(" 1st Funct call")
fun("C","C++")
print(" 2nd Func call")
fun("C","Java","Python")

    
