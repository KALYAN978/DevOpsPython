# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 10:03:56 2023

@author: kalypatn
"""

#Scope

enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1
    

increase_enemies()
print(f"enemies outside function: {enemies}")

#Local scope (local scope exists within the function)
def drink_potion():
    potion_strength = 2
    print(potion_strength)
    
  
    

player_health = 10
def drink_potion():
    potion_strength = 2
    print(player_health)
    print(potion_strength)
    
drink_potion()


#global constants
PI = 3.1415
URL = "https://www.google.com"




