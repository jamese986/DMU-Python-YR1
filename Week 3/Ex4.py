#Week 2 - Quick Exercise off of handout.
#A simple program that print make, name & registration as well as the name of the owner
#P14138928 - James English
#print greeting
print (\
"""
P A I N T  C A L C U L A T O R

""")

print('Enter the dimensions of the room in meters...')

#Getting user to input dimensions
#Converting from string to float
room_h = input("\nEnter the height of the room in meters: ")
room_h = float(room_h)

width_of_fw = input("\nEnter the width of the first wall: ")
width_of_fw = float(width_of_fw)

width_of_sw = input("\nEnter the width of the second wall: ")
width_of_sw = float(width_of_sw)
#End of user input section
total_area= float(width_of_sw * width_of_fw*2)

#Printing results to screen
print('\nThe total area of the walls in meters is %0.2f' %(total_area)+'.')
print("You will need %0.2f " %(total_area/10)+ "litres of paint.")

input("\nPress the enter key to exit...")
