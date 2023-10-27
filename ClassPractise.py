# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 16:36:32 2023

@author: kalypatn
"""

class Car:
    
    def __init__(self,company,Topspeed):
        self.company = company
        self.Topspeed = Topspeed
        
    
    def getInfo(self):
        self.company
        self.Topspeed


carobj1 = Car("Lamborghini","315kmph")
carobj1.getInfo()
print(carobj1.Topspeed)
print(carobj1.company)