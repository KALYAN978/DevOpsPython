# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 10:37:21 2023

@author: kalypatn
"""

#choosing a random number btw 1 and 100

#Make a function to set difficulty

#Let the user guess a number

# Function to check users guess against actual answer

#Track the number of turns and reduce by 1 if they get it wrong.

#Repeat the guessing functionality if they get it wrong



#choosing a random number btw 1 and 100
from random import randint
from logo import logoo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


#Make a function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty easy or hard: ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else :
        return HARD_LEVEL_TURNS


# Function to check users guess against actual answer
def check_answer(guess, answer, turns):
    """" checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else :
        print(f"You got it! The answer was {answer}")

def game():
    #choosing a random number btw 1 and 100
    print("Welcome to the Number guessing game")
    print("Im thinking of random number between 1 and 100.")
    answer = randint(1,100)
    print(f"Pssst, the correct answer is {answer}")
        
        
    #allowing the user to set the difficulty    
    turns = set_difficulty()
       
    
    
    #Repeat the guessing functionality if they get it wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number") 
        #now let the user guess the number
        guess = int(input("Guess a number: "))
        
        #Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(guess,answer, turns)  #we are updating the local variable every time we check the answer
        if turns == 0:
            print("You've run out of guesses, You lose")
            return
        elif guess != answer:
            print("Guess again.")
            
            
            
            
game()






        
