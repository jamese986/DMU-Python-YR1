# P14138626 - James English
# Loose silver change calculator

name = input("Hello, what's your name? ")

print ("\nThis is a stick-up ",name," empty your loose change onto the desk...\n")

#additional coins
one_pence = input("How many one pence coins do you have?: ")
one_pence =int(one_pence)
two_pence = input("How many two pence coins do you have?: ")
two_pence =int(two_pence)
five_pence = input("How many five pence coins do you have?: ")
five_pence = int(five_pence)
ten_pence = input("How many ten pence coins do you have?: ")
ten_pence = int(ten_pence)
twenty_pence = input("How many twenty pence coins do you have?: ")
twenty_pence = int(twenty_pence)                      
fifty_pence = input("How many fifty pence coins do you have?: ")
fifty_pence = int(fifty_pence)                      
#Additional coins
one_pound = input("How many pound coins do you have?: ")
one_pound = int(one_pound)
two_pound = input("How many two pound coins do you have?: ")
two_pound =int(two_pound)
#orginal lose change calculation
#loose_change = five_pence * 0.05 + ten_pence * 0.1 + twenty_pence * 0.2 + fifty_pence * 0.5

loose_change = one_pence * 0.01 + two_pence * 0.02 + five_pence * 0.05 + ten_pence * 0.1 + twenty_pence * 0.2 + fifty_pence * 0.5 + one_pound * 1.0 + two_pound * 2.0

print ("\nYou have: %0.2f in coins" % (loose_change))

input("\n\nPress the enter key to exit.")

