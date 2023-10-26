# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 15:38:51 2023

@author: kalypatn
"""

class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
        
    def funct(self):
        print(self.firstname,self.lastname)
        

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)  #It will inherit all the properties of Parent Class
        
        
x = Student("Firstname","Lastname")
x.funct()