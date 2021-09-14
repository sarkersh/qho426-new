"""
14 - Multiple User Defined Functions: Activity 1:
def display_box(name):
    message = "* Hello {} *".format(name)
    print("*" * len(message))
    print(message)
    print("*" * len(message))
def greet_user():
    print("Please enter your name")
    name = input()
    display_box(name)
greet_user()
Output:
****************
* Hello shakil *
****************
"""
def display_ladder(steps):
    # Display each step
    for step in range(steps):
        print("| |")
        print("***")
    # Display bottom of ladder
    print("| |")
def create_ladder():
    print("How many steps remain?")
    steps = int(input())
    display_ladder(steps)

create_ladder()














