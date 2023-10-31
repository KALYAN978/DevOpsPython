# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 14:34:49 2023

@author: kalypatn
"""

# Two preceeding Numbers
#eg: 1,1,2,3,5,8...

a = 0
b = 1

n = int(input("Enter n for how many times generate series: "))
print("Fibonacci Series")

print("",a," ",b,end = "")

for i in range(n):
    c = a + b
    a = b
    b = c
    print(" ",c, end = "")