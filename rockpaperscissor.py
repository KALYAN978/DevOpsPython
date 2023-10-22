# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 19:58:23 2023

@author: kalypatn
"""

import random

user_choice = int(input("what do you choose?"))

computer_choice = random.randint(0,2)

print(f"Computer choice: {computer_choice}")


if user_choice >= 3 or user_choice < 0:
    print("You type an invalid number you loose!!")
elif user_choice == 0 and computer_choice == 2:
    print("u wins!")
elif computer_choice == 0 and user_choice == 2:
    print("You loose")  
elif computer_choice > user_choice:
    print("You loose")
elif user_choice > computer_choice:
    print("you win")
elif computer_choice == user_choice:
    print("Its a draw")
elif user_choice >= 3 or user_choice < 0:
    print("You type an invalid number you loose!!")
