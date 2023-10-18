# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 10:40:48 2023

@author: kalypatn
"""

#Step 1

import random
word_list = ["ardvark", "baboon", "camel"]

#Todo-1 : Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list) 
word_length = len(chosen_word)

lives = 6

#Testing code
print(f"Psst, the solution is {chosen_word}.")


display = []
for _ in range(word_length):
    display += "_"

    
    
    
#Todo-2 : Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()


#Todo-3 : Check if the letter the user guessed (guess) is one of the letters in the choosen_word.
for position in range(word_length):
    letter = chosen_word[position]
    print(f"Current position: {position}\n Current letter: {letter}\n Guesses letter: {guess}")
    if letter == guess:
        display[position] = letter

if guess not in chosen_word:
    lives -= 1
    if lives == 0:
        end_of_game = True
        print("You lose")
        
print(f"{' '.join(display)}")


if "_" not in display:
    end_of_game = True
    print("You win.")
    
    
print(stages[lives])









