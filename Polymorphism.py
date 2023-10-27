# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 13:03:09 2023

@author: kalypatn
"""

# with polymorphism we can execute the same method for all classes.

# Different classes have the same method


class Car:
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    

    def move(self):
        print("Drive")


class Boat:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print("Sail")
        
class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Fly!")


car = Car("Ford", "Mustang")
boat = Boat("titanic", "Touring 20")
plane = Plane("KingFisher", "6576")


for x in (car,boat,plane):
    print(x.brand)
    print(x.model)
    x.move()
