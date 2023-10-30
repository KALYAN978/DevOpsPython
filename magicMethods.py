# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 12:13:11 2023

@author: kalypatn
"""

# str magic method
# str function --> object is converted into string

#magic methods --> starts and ends with __init__()

class Person:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name}{self.age}"
    
person = Person("kalyan","787")
print(person)

