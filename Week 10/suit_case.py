# suit_case.py
# Demonstrates tuples
# by Dawn

# create a tuple with some items and display with a for loop
suit_case = ("shirt",
             "trousers",
             "tooth brush",
             "pyjamas")
print ("Your suit case contains:")
for item in suit_case:
    print (item)

input("\nPress the enter key to continue.")

# get the length of a tuple
print ("You have", len(suit_case), "items in your possession.")

input("\nPress the enter key to continue.")

# test for membership with in
if "pyjamas" in suit_case:
    print ("\n\nYou've packed your pyjamas")
    print ("...now you won't have to sleep in your shirt!")

# display one item through an index
index = int(input("\nEnter the index number for an item in suit_case: "))
print ("At index", index, "is", suit_case[index])

# display a slice
begin = int(input("\nEnter the index number to begin a slice: "))
end = int(input("Enter the index number to end the slice: "))
print ("suit_case[", begin, ":", end, "]\t\t",)
print (suit_case[begin:end])

input("\nPress the enter key to continue.")

# concatinate two tuples
coat_pocket = ("passport", "mobile phone")
print ("You look in your coat pocket.  It contains:")
print (coat_pocket)
print ("\nYou add the contents of your coat pocket to your suit case.")
suit_case += coat_pocket
print ("Your suit_case now contains:")
print (suit_case)


# get the length of a tuple
print ("\n\nYou now have", len(suit_case), "items in your possession.")

input("\n\nPress the enter key to exit.")


