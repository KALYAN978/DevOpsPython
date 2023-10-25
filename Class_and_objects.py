# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 11:15:14 2023

@author: kalypatn
"""

#introduction to the class

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    #def __str__(self):
     #   return f"{self.name}({self.age})"
     
    def myfunc(self):
        print("HI kalyan")

p1 = Person("kalyan", 23)
#print(p1.age)
#print(p1.name)
print(p1)
p1.myfunc()