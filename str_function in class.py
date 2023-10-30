# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 11:51:21 2023

@author: kalypatn
"""

class Person:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name}{self.age}"

p = Person("aklyan",23)
#print(p.name)
#print(p.age)

print(p)