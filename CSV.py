# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 11:41:03 2023

@author: kalypatn
"""

#CSV
#Comma separated Values -> used for storing data in table

import csv


with open('data.csv','r') as file:
    reader = csv.reader(file)  #we have a csv.reader object using csv.reader() function
    
    for row in reader:
        print(row)