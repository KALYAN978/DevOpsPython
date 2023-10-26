# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 12:23:30 2023

@author: kalypatn
"""

class Car:
    
    car = "Super Car"
    
    # Creating a constructor for this class
    def __init__(carType, company, TopSpeed):
        carType.company = company
        carType.TopSpeed = TopSpeed
        

#Creating the Objects for this class
carobj1 = Car("Lamborghini", "350kmph")
carobj2 = Car("Bugatti", "415kmph")

print("printing carobj1 details: ")
print(carobj1.car)
print(carobj1.company)
print(carobj1.TopSpeed)
print("printing carobj2 details: ")
print(carobj2.car)
print(carobj2.company)
print(carobj2.TopSpeed)


