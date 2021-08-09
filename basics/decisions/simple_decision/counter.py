# Ask user to enter whole number
first_number = int(input())
second_number = int(input())
third_number = int(input())

e_numbers = 0
o_numbers = 0

# Determine which numbers are even and which are odd

if first_number % 2 == 0:
    e_numbers = e_numbers + 1
else:
    o_numbers = o_numbers + 1

if second_number % 2 == 0:
    e_numbers = e_numbers + 1
else:
    o_numbers = o_numbers + 1

if third_number % 2 == 0:
    e_numbers = e_numbers + 1
else:
    o_numbers = o_numbers + 1

# Display result
print("There were {} even and {} odd numbers.".format(e_numbers, o_numbers))
print(f"There ware {e_numbers} even and {o_numbers} odd numbers.")











