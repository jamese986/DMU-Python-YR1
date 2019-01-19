# Excercise 2 - Converter
# Pinta to Litres conversion
# P14138628 - James English

#print greeting
print (\
"""
P I N T S  T O  L I T R E S  C O N V E R S I O N
""")

#convert value pints from string to float
pints = input("Enter the amount in pints: ")
amount_of_pints = float(pints)

#pints to litres conversion
litres = float ('0.568')
total = amount_of_pints*litres

#print conversion
print ("\n"+pints +" pints is equivalent to %0.2f" %+(total)+' litres')

input ("\nPress the enter key to exit.")
