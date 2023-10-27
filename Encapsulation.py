# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 12:50:21 2023

@author: kalypatn
"""

class Students:
    
    def __init__(self,name,rank,points):
        self.studentname = name
        self.studentrank = rank
        self.studentpoints  = points
        
    
    def demofunction(self):
        print(f"I am  {self.studentname}")
        print(f"I got Rank   {self.studentrank}")
        

st1 = Students("ram", 1, 100)
st2 = Students("lakshman", 2, 100)


st1.demofunction()
st2.demofunction()