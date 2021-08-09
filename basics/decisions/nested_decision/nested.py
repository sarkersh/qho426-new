# ask user what to do
"""print("What should I do (play/study)?")
activity = input("play/study: ")

# Decide if beep should play or study
if (activity == "play"):
    # Ask user what to play with
    print("What should I play with (toy/friend)?")
    play_with = input("toy/friend: ")
    # Decide if beep should play with toy or friend
    if(play_with == "toy"):
        print("I will play with toys!")
    else:
        print("I will play with my friend!")
else:
    print("I will study")"""
#######################################################

print("What type of cover does the book have(hard or soft)?")
cover_type = input("hard/soft:")
if(cover_type == "soft"):
    print("Is the book perfect-bound?")
    answer = input("yes/no: ")
    if(answer == "yes"):
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books!")
else:
    print("Books with hard covers can be more expensive!")




























