# Activity 3: Range
"""
range(1, 10, 1) produces the following list of numbers: 1, 2, 3, 4, 5, 6, 7, 8, 9 (natural numbers)
range(1, 10, 2) produces the following list of numbers: 1, 3, 5, 7, 9 (odd numbers)
range(0, 10, 2) produces the following list of numbers: 0, 2, 4, 6, 8 (even numbers)

"""
# Ask user for brightness level
print("What level of brightness is required?")
n = int(input())  # n = desired brightness
# Adjust brightness
print("\nAdjusting brightness...\n")
for b in range(2, n+1, 2):
    print("Beep's brightness level:",b*"*")
    print("Bop's brightness level :", "*"* b)
print("\n\nAdjustments complete!")