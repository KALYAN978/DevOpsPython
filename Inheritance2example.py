# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 13:41:23 2023

@author: kalypatn
"""

class Car:
    
    def __init__(self,comp,mod):
        self.company = comp
        self.model = mod
        
    def getInfo(self):
        self.company
        self.model
        
        
car1 = Car("Lamborghini","djaskdh")
car2 = Car("Bugatti", "Ushaku")

car1.getInfo()
car2.getInfo()