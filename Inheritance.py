# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 15:27:32 2023

@author: kalypatn
"""

class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
        print(self.firstname,self.lastname)
    
class Student(Person):
    pass

s = Student("kalyan","Js") 
print(s.firstname)
s.printname()