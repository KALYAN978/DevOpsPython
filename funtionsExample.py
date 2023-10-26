# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 10:56:39 2023

@author: kalypatn
"""

#Functions example

#def printMessage():
#    print("python")
    
#printMessage()


#==== Passing values to the function ===========

#def sum(a,b):
#    ans = a+b
#    print(ans)

#sum(1,2) 

#num  = 1
#num1 = 2

#sum(num, num1)



#========= Recursive Functions =============

#def add(n):
#    if n != 0:
#        return n + add(n-1)  #Returning Value of the function itself
#    else:
#        return n
    
#ans = add(10)
#print(ans)





#========== Returning values from function  ================

def sum(a,b):
    ans = a + b
    return ans

Ans = sum(1,4)
print(Ans)