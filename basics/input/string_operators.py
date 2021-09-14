# Read bot data
print("Please enter number of lives")
lives = int(input())

print("Please enter energy level")
energy = int(input())

print("Please enter shield level")
shield = int(input())

# Display bot data
print(f"Lives:  {'♥' * lives}")
print(f"Energy: {'♦' * energy}")
print(f"Shield: {'♦' * shield}")
