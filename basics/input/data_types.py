# Read in user data
print("What is your name?")
name = input("My name is ")

print("What is your age?")
age = int(input("My age is "))

print("What is your weight?") 
weight = float(input("My weight is "))

print("What is your height?")
height = float(input("My height's "))

# Calculate bmi
bmi = weight / (height ** 2)

# Display result
print(f"{name} your bmi is {bmi:.2f}")
