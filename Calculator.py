# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 21:15:12 2023

@author: kalypatn
"""




#Calculator

#Add 
def add(n1,n2):
    return n1+n2

#subtract
def subtract(n1,n2):
    return n1-n2

#multiply
def multiply(n1,n2):
    return n1*n2

#division
def divide(n1,n2):
    return n1/n2


#creating a dictionary named operations
operations = {
 "+": add,
 "-": subtract,
 "*": multiply,
 "/": divide
}

()
function = operations["*"]
function(2,3)  #now this function act as a mutlitply function


num1 = int(input("WHat's the first number? :"))
num2 = int(input("What's the second number? :"))

for symbol in operations:
    print(symbol)
    
operation_symbol = input("Pick an operation from the line above: ")

calculation_function = operations[operation_symbol]
answer = calculation_function(num1,num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")
    



