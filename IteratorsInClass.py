# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 12:13:09 2023

@author: kalypatn
"""

# Iterators in class

# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.

class MyNumbers:
    
    def __iter__(self):
        self.a = 1     #initializing a attribute a to 1
        return self
    
    def __next__(self):   #we are getting the next item in the iteration
        x = self.a        #self.a represents current number in the sequence & starts at 1
        self.a += 1     
        return x         # previous value before incrementing is the "next" value in the iteration.         
    

numbers = MyNumbers()
myiter = iter(numbers)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


#if you have an instance numbers and create an iterator myiter, calling next(myiter) will return 1,
# the first value in the sequence. Subsequent calls to next(myiter) will return 2, 3, 4, and so on, 
#as self.a is incremented with each call.