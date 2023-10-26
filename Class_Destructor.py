# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 12:44:06 2023

@author: kalypatn
"""

class Destructor:
    
    #Initializing The Constructor
    def __init__(self):
        print("Constructor called")
        
    def __del__(self):
        print("destructor called")
        
dobj = Destructor()
print("deleting obj")

del dobj