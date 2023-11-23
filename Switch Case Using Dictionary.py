# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 10:51:21 2023

@author: kalypatn
"""


myswitch = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five"
    }

num = int(input("Enter any Number from 1 to 5: " ))

print("You Enter :", myswitch.get(num,"Invalid Number"))

