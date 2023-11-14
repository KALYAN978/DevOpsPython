# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 14:35:17 2023

@author: kalypatn
"""

def outerFun():
    print("hello from Outer Function")
    
    def innerFun():
        print("Hello From Inner function")
        
    innerFun()
    
    
outerFun()