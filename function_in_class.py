# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 15:22:43 2023

@author: kalypatn
"""

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    
    def func(self):
        print("hello")
        
    def printname(self):
        print(self.age,self.name)
        
p = Person("Kalyan", 24)
print(p.age)
print(p.name)
p.func()
