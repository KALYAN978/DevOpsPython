# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 13:15:13 2023

@author: kalypatn
"""

# polymorphism in inheritance class

class Vehicle:
    
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print("Move")
        
class Car(Vehicle):
    pass


class Boat(Vehicle):
    def move(self):
        print("sail")


class Plane(Vehicle):
    def move(self):
        print("fly")
        
        
        
car = Car("ford", "Mustang")
boat = Boat("titanic", "Tiuri 3743")
plane = Plane("Kingfisher", "67576")


for x in (car,boat,plane):
    print(x.brand)
    print(x.model)
    x.move()        #overriding the move() in Boat and Plane class