# Activity 4: Characters
"""
user_string[0]
Where user_string is variable of data type string and the number 0 is the index number of the first character in the
string. A loop can be used to iterate through each character in a string. For example, let us assume we wish to display
each character in a string entered by a user. We could do the following:
print("Please enter a word")
user_word = input()
for p in range(0,len(user_word), 1): # p = positions
    print(user_word[p])
In the above code a for loop is used to iterate through a range of numbers from 0 up to, but not including,
the length of user_word. These numbers represent the position of each of the characters in the word. Hence, the position
is used to index and display a character in user_word with the first character at an index of 0.
"""
# Ask user for markings
print("What strange markings do you see?","\n♯☼⌂╝ℓ\n\nIdentifying...")
markings = input()
for count in range(0, len(markings), 1):
    print("index", count, ":", markings[count])
print("\nDone!")














