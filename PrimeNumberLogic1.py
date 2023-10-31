# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 14:06:39 2023

@author: kalypatn
"""

#primeNumber logic1

count = 0

n = int(input("Enter a number: "))

for i in range(1,n+1):
    if n%i == 0:
        count += 1
if count == 2 :
    print(n, "is a prime number")
else:
    print(n, " is not a prime Number")
    