# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 12:44:32 2023

@author: kalypatn
"""

#Review
#create a function called greet()
#write 3 print statements inside a function
#call the greet() function and run your code.

def greet():
    print("Hello")
    print("How do uou do?")

greet()

#Function that allows for input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    
greet_with_name("Kalyan")


#Functions with more than 1 input
def greet_with(name,location):
    print(f"Hello {name}")
    print(f"what is ur {location}")
    
greet_with("Kalyan", "India")

#positional arguments
greet_with("hyderabad", "Kalyan")

#Keyword Arguments
greet_with(location = "hyderabad", name = "kalyan")