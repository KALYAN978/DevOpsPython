# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 14:27:16 2023

@author: kalypatn
"""

programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", 
                          "Function": "A piece of code that you can easily call over and over again."}


#For printing the elements in the index is  as same as the printing array
 #How to print an element in the dictionary
print(programming_dictionary["Bug"])


#Adding new items into the Dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"

#Creating an empty dictionary.
empty_dictionary = {}

#wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)


#Editing an item in dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)


#Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
    
    
 