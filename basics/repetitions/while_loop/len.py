# Activity 4: Repeating Word , we use today another built in function is the len() function.
# This function will return the number of items in an object.  If the object is a string then
# this function will return the number of characters in the string.  For example, len( "Beep")
# will return 4 as there are 4 characters in the string "Beep".

# Ask user for phrase
print("Please enter a phrase:")
phrase = input()

# Declare a control variable
bops = 0

# Display Bops
print()

# while loops
while(bops < len(phrase)):
    print("Bops ", end="")
    bops = bops + 1