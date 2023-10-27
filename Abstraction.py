# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 13:33:15 2023

@author: kalypatn
"""

# Python provides the "abc" module to use the abstraction in the Python program.

# abstract base class work

from abc import ABC, abstractmethod  #importing abc module to create abstract base class

class Car(ABC):
    def mileage(self):   #defining abstract method 
        pass
    

class Tesla(Car):
    def mileage(self):
        print("Mileage is 300kpmh")


class Suzuki(Car):
    def mileage(self):
        print("Mileage is 200kmph")
        
        
class Duster(Car):
    def mileage(self):
        print("Mileage is 240kmph")


T = Tesla()
S = Suzuki()
D = Duster()


T.mileage()
S.mileage()
D.mileage()

