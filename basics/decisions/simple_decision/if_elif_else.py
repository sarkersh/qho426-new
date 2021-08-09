# IF...ELIF...ELSE statement

first_number = 8
second_number = 8

if (first_number > second_number):
    print("First is bigger!")
elif (first_number < second_number):
    print("First is smaller!")
else:
    print("Both are equal!")
print("Done!")
# let us consider another example:

entity = input()

if (entity == "Human"):
    print("You are a human!")
elif (entity == "Robot"):
    print("You are a robot!")
elif (entity == "Animal"):
    print("You are an animal!")
else:
    print("I do not know what you are!")
print("Analysis complete.")
# Tasks if_elif_else
# Ask user for direction
print("Towards which direction should I paint (up, down, left or right)?")
direction = input()
if(direction == "up"):
    print("\nI am painting in the upwards direction!")
elif(direction == "down"):
    print("\nI am painting in the downwards direction!")
elif (direction == "left"):
    print("\nI am painting in the leftward direction!")
elif (direction == "right"):
    print("\nI am painting in the rightward direction!")
else:
    print("\nNot sure which direction I am painting in!")















