#Python Exercise 4
#Mini program to get user input
#P14138628 - James English

#print greeting
print (\
"""
T E M P E R A T U R E  C O N V E R S I O N

""")
#getting user input and converting string to integer
temp = input("Enter the temperature: ")
temp =float(temp)

#converting Celsius to Fahrenheit
c_to_fh = float(temp*9/5+32)

#converting Fahrenheit to Celsius
fh_to_c = float(temp-32)*(5/9)

print(str(temp) +" degrees Celsius = %0.2f" %float(c_to_fh)+' Fahrenheit.\n')
print(str(temp)+" degrees Fahrenheit= %0.2f" %float(fh_to_c)+' Celsius.')

input("\n\nPress the enter key to exit.")
