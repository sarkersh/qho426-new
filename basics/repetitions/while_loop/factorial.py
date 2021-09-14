# Activity 7: Factorial
# Displaying the message
print("Please enter a number:")
number = int(input())
# Calculate factorial
count = 0
total = 1
while(count < number):
    count = count + 1
    total = total * count
# Display result
print(f"The factorial is {total}")
