# Activity 2: Logical AND operator
# Retrieve size and weight from user
print("What size is the parcel?")
size = input("big/small: ")
print("What is weight of the parcel?")
weight = input("heavy/light: ")
# Identify and display the category
if ((size == "big") and (weight == "heavy")):
    print("This parcel will be expensive to deliver.")
else:
    print("This parcel will be inexpensive to deliver.")
#########################################################
# Task:
print("What did I hear?")
u_response1 = input()
print("What did I see?")
u_response2 = input()
if ((u_response1 == "grrr") and (u_response2 == "two red eyes")):
    print("There is a scary creature. I should get out of here!")
else:
    print("I am a little scared but I will continue.")






















