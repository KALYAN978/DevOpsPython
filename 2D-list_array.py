# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 11:27:01 2023

@author: kalypatn
"""


#Types of list
#1-D List
#Language = ["c","C++"]

#2-D List
#Employee = [["kalyan", "cap"],["shawn","uk"]]


#2D - list(array)

population  = [["1","china"],["2","india"],["3","USA"]]

i = 0
j = 0

while i<3:
    
    while j < 2:
        print(population[i][j], end = "")
        j = j+1
        
    i = i + 1
    j = 0
    print()