# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 15:32:42 2023

@author: kalypatn
"""

class Person:
    
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
        print(self.firstname,self.lastname)
    

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        
x = Student("kalyan", "KALYAN")
print(x.firstname)
x.printname()