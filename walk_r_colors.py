# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 13:38:05 2023

@author: kalypatn
"""
import turtle as t
import random

tim = t.turtles()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color
    
    
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random.color())
    tim.forward(30)
    tim.sethead(random.choice(directions))
    


