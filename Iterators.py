# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 11:38:10 2023

@author: kalypatn
"""

#Iterators is an object that contains a countable number of values

#Iterator methods : __iter__() and __next__()




mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)


# next() is used to retreive the next element from the iterator

print(next(myit))   #after printing apple iterator is placed at the banana element
print(next(myit))   
print(next(myit))




