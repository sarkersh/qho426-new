#################################################
# function can either return a value or not
#################################################

# if a function does not return anything
# there is no return statement inside of that function
def print_separator(x):
    print('~' * x)

# calling it
print_separator(20)



# if a function returns a value,
# it must be called in a different way
def get_rate(x):
    c = x * 10
    return c

# two ways of callint it
# either save into a variable...
rate = get_rate(5)
# ...or print it
print('New rate is:', get_rate(5))
# functions that return a value cannot be called just like this
# get_rate(5)