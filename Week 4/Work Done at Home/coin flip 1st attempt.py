# P14138628 - James English
# Coin Flip Exercise 
# Deonstrates while loop and nested if statment. 

#print greeting
print (\
"""
C O I N  F L I P  G A M E 

""")
#importing the random module.
import random

#getting user input and converting into int
user_flips = input("How many times do you want to flip the coin? ")
user_flips = int(user_flips)

# defining heads and tails to variables
tails = 0
heads = 0

#while loop limiting the amount of flips to user_flips
while  heads + tails != user_flips:
    chance = random.randrange(2)
    #if / else statement adding 1 if condition is meet 
    if chance == 0:
         heads += 1
    else:
        tails += 1

#printing outcomes
print('The coin was flipped ' +str(user_flips) + ' times.')
print('the number of heads was ' +str(heads)+',')
print('the number of tails was ' +str(tails)+'.')

print('\nThank you for playing the Coin Flip Game.')
input("\nPress the enter key to exit.")

