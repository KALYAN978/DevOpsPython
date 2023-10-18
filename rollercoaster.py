# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 12:41:39 2023

@author: kalypatn
"""

print("Welcome to the roller coster")
height = int(input("what is your height in cm>?:"))

if(height >= 120):
    print("You can ride the roller coaster")
    age = input("what is your age?:")
    if age < 12:
        bill = 5
        print("Child tickets are Rs5")
    elif age <= 18:
        bill = 7
        print("youth tickets are Rs7")
    else:
        bill = 12
        print("Adult tickets are Rs12")
        
    wants_photo =input("Do you want to take photos? Y or N :")
    if wants_photo == "Y":
        bills = bill + 3
    
else:
    print("You cannot rider the roller coaster")