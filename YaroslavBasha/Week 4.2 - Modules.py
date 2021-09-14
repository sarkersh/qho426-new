#################################################
# modules
#################################################

# user defined functions can be stored in a file
# called module
# to use functions from that module,
# you need to import that module

# to import module
import random

# now you can use any function from that module
# you need to call module_name.function_name():
print(random.randrange(1,100,1))


# import module and give it a short name (alias)
import random as rn

# to call function here,
# you put alias.function_name():
print(rn.randrange(1,100,1))


# importing user-defined module
import fn
fn.supermegafunction('#', 30)


# it is possible to import multiple modules in a single import statement
import math


# to import a specific function from a module,
# without importing all other functions from the same module,
# use keyword from:
print(math.sin(45))
# you can still assign an alias to it:
from math import sin as sine
print(sine(60))