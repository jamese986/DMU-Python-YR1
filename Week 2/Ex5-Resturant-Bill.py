# Excercise 2 - Restaurant bill calculator 
# Demonstrates type conversion
# P14138628 - James English


#print greeting
print (\
"""
R E S T A U R A N T   B I L L   C A L C U L A T O R 

Enter the amount the customer spent for each part of the meal...

""")

#convert value for starter into a float
starter = input("starter: ")
starter = float(starter)

#convert value for main meal into a float
main_meal = input("Main meal: ")
main_meal = float(main_meal)

#convert value for dessert into a float
dessert = input("Dessert: ")
dessert = float(dessert)


#calculate the total price of the meal by adding the starter the main and dessert
#values together.
total = starter + main_meal + dessert
incvat = total/100*20

#print grand total and set cost to 2 decimal places.
print ("\nGrand Total (excl VAT): %0.2f" % (total))

#print grand total excl VAT and set cost to 2 decimal places.
print ("\nGrand Total (incl VAT): %0.2f" % (total + incvat))

#  The %0.2f in the print statement above formats the floating-point number
#  so that only two digits appear after the decimal point.
#  It is called a string format operator.

input("\n\nPress the enter key to exit.")
