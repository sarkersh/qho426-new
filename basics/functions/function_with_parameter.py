"""
Activity 3: Parameters : A parameter (also known as a formal argument) is an input to a function. Parameters allow us to
pass information into functions.  Parameters are set when the function is called with suitable values
(also known as actual arguments).The diagram below shows how a function can be invoked in Python:
https://learn.solent.ac.uk/pluginfile.php/2793911/mod_page/content/6/functions-and-arguments.png
"""
def escape_by(plan):
    if(plan == "jumping over"):
        print("We cannot escape that way! The boulder is too big!")
    elif(plan == "running around"):
        print("We cannot escape that way! The boulder is moving too fast!")
    elif(plan == "going deeper"):
        print("That might just work! Let's go deeper!")
    else:
        print("We cannot escape that way! The boulder is in the way!")

escape_by("jumping over")
escape_by("running around")
escape_by("going deeper")