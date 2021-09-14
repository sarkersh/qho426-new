"""
Activity 2: ASCII character

It is also possible to convert an ASCII code back into a character.

"""
print("Program Started!")
print("Please enter an ASCII code:")
code = int(input())
if(code >= 32 and code <= 126):
    print("The character represented by the ASCII value {} is: {}".format(code, chr(code)))
else:
    print("Error, please input number range between 32 to 126!")
print("Program Ended!")
