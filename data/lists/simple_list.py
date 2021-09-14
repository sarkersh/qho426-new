"""
Activity 1: Simple List
A list is a data structure that stores elements in the order in which they are inserted.
In python, we can create a list using square brackets [ ].
For example, we can create an empty list and assign this to a variable named fruits as follows:
"""
fruits = []
# We can also initialise our list with some items by providing these between the square brackets:
fruits = ["apple", "banana", "cherry"]
# We can add an item to the end of an existing list by using the append method (a function) of list:
fruits.append("dragon fruit")
# Similarly, we can remove an existing item from our list using the remove method (a function)
# of list which will remove the first occurrence of the item:
fruits.remove("banana")
print(fruits)
# Task:
def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions
def run():
    print(directions())
run()