# Ask user for distance
print("How far are we from the cave?")
distance = int(input())
# Display count down
print()
for step in range(distance,0,-1):
    print(step,"steps remaining")
print("We have reached the cave!")