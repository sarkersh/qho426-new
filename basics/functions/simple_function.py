"""
13 - User Defined Functions
Activity 1: Simple User Defined Function

In Python, functions can be defined by using the keyword def, a function name and
zero or more parameters (inputs to the function). As a simple example, consider the following
program to display a greeting:
"""
print("Please enter your name")
name = input()
print("Hello", name)
######################## We can turn above this to a function as follow: ###############################################
# The function
def greet_user():
    print("Please enter your name")
    name = input()
    print("Hello", name)

# Call to function
greet_user()
######################## Task: #########################################################################################
def listen():
    print("What sound did I hear?")
    sound = input()
    print("\nThat was a loud", sound)

listen()
