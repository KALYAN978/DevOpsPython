# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 22:38:30 2023

@author: kalypatn
"""

from tkinter import *

window = Tk()


r = Label(bg = "red", width = 20, height = 5)
r.grid(row = 0, column = 0)

g =Label(bg = "green", width = 20, height = 5)
g.grid(row = 1, column = 1)

b = Label(bg = "blue", width=40, height = 5 )
b.grid(row=2, column=0, columnspan = 2)     #columnspan = how many columns this particular thing will occupy


window.mainloop()





