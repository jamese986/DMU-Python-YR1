# P14138628 - James English
# craps_roller.py
# Demonstrates random number generation

import random

# generate random numbers 1 - 6
die1 = random.randrange(6) + 1    
die2 = random.randrange(6) + 1

#Adding the 2 dice rolls together
total = die1 + die2

#Prints the result to the screen
print ("You rolled a", die1, "and a", die2, "for a total of", total)

input("\n\nPress the enter key to exit.")
