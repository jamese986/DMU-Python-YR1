# P14138628 - James English
# Fortune Cookie Simulator

#print greeting
print (\
"""
W E L C O M E  TO  T H E  F O R T U N E  C O O K I E  S I M U L A T O R. 

""")
import random

#getting users name
name = input("Please enter your name here. ")

#setting fortune to be a random number between 0-5
fortune = random.randrange(6)

#Loop to select a fortune at random.
if fortune ==0:
    #fortune 1
    print=(name +" you can never been certain of success, but you can be certain of failure if you never try.")

elif fortune ==1:
    #fortune 1
    print(name +" your pain is the breaking of the shell that encloses your understanding.")

elif fortune ==2:
    #fortune 2
    print(name +" love can turn cottage into a golden palace.")

elif fortune ==3:
    #fortune 3
    print(name+ " fortune favors the brave.")

elif fortune ==4:
    #firtune 4
    print(name+ " what ends on hope does not end at all.")

else:
    #fortune 5
    print(name+ " this is really a lovely day. Congratulations.")

print('\nHave a Good Day ' +name +'... Goodbye.')
