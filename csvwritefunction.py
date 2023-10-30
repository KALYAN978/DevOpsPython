# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 11:46:18 2023

@author: kalypatn
"""

#csv write function

import csv

data = [['Name','Age','Country'],["Alice","25","USA"],
        ["Bob","30","canada"],["charlie","35","Australia"]]

with open('data.csv','w') as file:
    writer = csv.write(file) #created csv.writer object using csv.writer function
    
    for row in data:
        writer.writerrow(row)