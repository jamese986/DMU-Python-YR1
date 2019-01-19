#Week 10 - Exercise 1
#Word Games Program
#P14138628 - James English

#importing the random module
import random

#Possible random words to chose from
words =("apple","pear","grapes")

#picking a random word
word = random.choice(words)

print(len(word))

#Getting users guess
user_a = input("enter your guess here ")

#testing to see if guess is correct
if user_a == word: 
   print("Yes!")
else:
   print("No")

input=("\nPress the enter key to continue. ")
