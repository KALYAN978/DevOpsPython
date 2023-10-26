# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 12:02:11 2023

@author: kalypatn
"""

#========== Creating a file ==================

#file = open('python.txt',"w")

#print("f")



#============ Deleting a file ==================

import os

if os.path.exists("python.txt"):
    os.remove("python.txt")
    print("file deleted successfully")
else:
    print("file not found")
    
    
    
#============== Reading a file ================

f = open("python.txt","r")

data = f.read()
print(data)




#================== Writing a file  ================

f = open("python.txt","a")
f.write("Write the message here")
print("file written successfully")

    
    