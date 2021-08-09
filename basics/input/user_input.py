# Ask user to enter their name
"""
print("What is your name human?")
name = input()
print("It is nice to meet you human", name)
"""
# Read in user's name
name = input("What is your name human?")
print("It is nice to meet you human", name, ".")
# With + operator
print("It is nice to meet you human" + name + ".")
# We can fix it as follow:
print("Nice to meet you " + name + ".")
# Our previous code can be re-written as follows:
print("Nice to meet you {}.".format(name))
# Python String format() Method : Insert the price inside the placeholder, the price should be in fixed point,
# two-decimal format :

txt = "For only {price:.2f} dollars!" # Here .2f means .00 price  must be like 49.00
print(txt.format(price=49))
"""----------------------------------------------------------------------------------------------------------------"""
# Ask user for name
print("What is your name?")
# Read user's response
name = input()
# Display confirmation message
print(f"Nice to meet you {name}")
