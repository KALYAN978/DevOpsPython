# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 15:04:14 2023

@author: kalypatn
"""

class Base:
    def cal_sum(self,a,b):
        return a+b
    
class Derived(Base):
    def cal_mul(self,a,b):
        return a*b
    
    
n1 = int(input("Enter 1st No: "))
n2 = int(input("Enter 2nd No: "))

d = Derived()

print(d.cal_mul(n1, n2))
print(d.cal_sum(n1, n2))