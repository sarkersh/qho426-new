# EXAMPLES of functions
#
# this code uses two functions:
# len() and expression()
# one of them is built-in, another one is user-defined
# can you tell which one is built-in and which one is user-defined?

prompt = "Hello, World"
print(len(prompt))
# this function will calculate 2a + b
def elephant(a,b):
  c = 2*a + b
  return c

print("Here is the result:", elephant(0, 500))
print("=============================")
age = input("Please input your age: ")
print("=============================")
city = input("Please input your city: ")
print("=============================")


def print_separator():
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print_separator()
age = input("Please input your age: ")
print_separator()
city = input("Please input your city: ")
print_separator()

# Function is a named piece of code. Benefits of functions:
# 1.	Reusing the code (to avoid copy-pasting)
# 2.	Single point of control over the code which
# 	otherwise would have been copy-pasted multiple times
# 3.	Restructuring the program
# 	into more manageable and more readable blocks:

# init();
# db_connect();
# get_user_input();
# validate_user_input();
# get_request();
# build_output();
# send_response();
# 4.	Applying the same algorithm to the different inputs
# y(x) = 3x + 2
# x=0, y -> 2
# x=1, y -> 5
# x=-1,y ->-1

# def y(x):
#     #output = 3*x + 2
#     #return output
#     return (3*x + 2)



# 5.	Separating scopes of variables
# 6.	Encapsulating logic, when a function can be used
# 	without knowing the details of how it works