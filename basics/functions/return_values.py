"""Activity 2: Return Values (~ minutes) :  A function can return a value.  This is useful when we wish to return a
result to a calling function (the caller) from a called function.  We can do this by using the keyword return.
For example, let us say we have a function that retrieves the name of a user.  Such a function may be coded as follows:
def get_name():
  print("Please enter your name")
  name = input()
  return name
print("Retrieved name:", get_name())
The above example the return keyword is used to return the value inputted by the user.
When a function returns a value, the original function call is replaced by the value returned by the called function.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Task:~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
def sum_weights(beep_weight, bop_weight):
    total_weight = beep_weight + bop_weight
    return total_weight

def calc_avg_weight(beep_weight, bop_weight):
    avg_weight = (beep_weight + bop_weight) / 2
    return avg_weight

def run():
    # retrieve required user data
    print("What is the weight of Beep?")
    beep_weight = float(input())

    print("What is the weight of Bop?")
    bop_weight = float(input())

    print("What would you like to calculate (sum or average)?")
    action = input()

    # determine and carry out action
    if (action == "sum"):
        answer = sum_weights(beep_weight, bop_weight)
        print("The sum of Beep's and Bop's weight is {:.2f}".format(answer))
    elif (action == "average"):
        answer = calc_avg_weight(beep_weight, bop_weight)
        print("The average of Beep's and Bop's weight is {:.2f}".format(answer))
    else:
        print("I am not sure what you would like to do.")
run()










