"""
Activity 5: Multiple Parameters : Task :
"""
def climb_ladder(a,b): # where a represents steps_remaining and b represents steps_crossed
    if(a > b):
        print("Still some way to go!")
    else:
        print("We are almost there!")

climb_ladder(5, 2)
climb_ladder(2, 5)