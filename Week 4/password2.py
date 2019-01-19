# P14138628 - James English
# password2.py
# Demonstrates the if-else structure

#prints welcome message to the screen
print ("Welcome to DeMontfort Security Ltd.")
print ("-- where security is our middle name\n")

#Takes password from user 
password = input("Enter your password: ")

#if-else statement to control what passwords are allowed
#Prints Access Granted/Denied depending on input
if password == "letmein":
   print ("Access Granted")
else:
   print ("Access Denied")
    
input("\n\nPress the enter key to exit.")
