
# Display start message
print("How many numbers should I sum up?")

# Ask user for number to sum
number_to_sum = int(input())

# Declare a control variable
summed = 0

# Display blank line
print()

# Sum numbers
total = 0

# while loop
while(summed < number_to_sum):
    print(f"Please enter number {summed} of {number_to_sum} : ")
    number = int(input())
    total = total + number
    summed = summed + 1

# Display result
print(f"The answer is {total}")
