"""
Activity 2: Indexing: As a list is indexed based, we can use the index corresponding to the position of an element in a
list to access, update or delete an item.  As indexes start from 0, the first element is accessed using [0]. The second
element is accessed using [1] and so on. # Display the first item i.e. apple :-
"""
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
# Update the second item i.e. replace banana with berry
fruits[1] = "berry"
# Remove the third item i.e. removes cherry
del fruits[2]
print(fruits)
fruits = ["apple", 5, "banana", 10, "cherry", 15]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Without loop:
def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path
def run():
    print("Moving...")
    path = movements()
    print(f"{path[0]} for {path[1]} steps")
    print(f"{path[2]} for {path[3]} steps")
    print(f"{path[4]} for {path[5]} steps")
    print(f"{path[6]} for {path[7]} steps")

run()
# With index loop:
def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path
def run():
    print("Moving...")
    path = movements()
    for index in range(0, len(path), 2):
        print(f"{path[index]} for {path[index+1]} steps")

run()


