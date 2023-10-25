# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 22:06:26 2023

@author: kalypatn
"""

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("its a prime number")
    else:
        print("its not a prime number")

n = int(input())

prime_checker(number = n)