"""
Multiple Conditions
Activity 1: Logical "or" Operator
we can implement decisions with multiple conditions using logical (and/or/not) operators.
he logical operators work by evaluating expressions from the left to the right.
In the case of the "and" operator the expressions on both sides of the operator must evaluate to True.
In the case of the "or" operator an expression on other side of the operator must evaluate to True.
In the case of the "not" operator only one of the expressions must evaluate to True.
"""
# Retrieve shape from user
print("What shape do I have?")
shape = input()
# Identify the shape
if ((shape == "square") or (shape == "rectangle") or (shape == "rhombus")):
    print("This shape is a parallelogram.")
else:
    print("This shape is not a parallelogram.")
# Ask user for the type of adventure
print("What type of adventure should I have?")
adventure_type = input()

# Determine what message to display
if ( (adventure_type == "scary") or (adventure_type == "short") ):
    print("\nEntering the dark forest!")
elif ( (adventure_type == "safe") or (adventure_type == "long") ):
    print("\nTaking the safe route!")
else:
    print("\nNot sure which route to take.")