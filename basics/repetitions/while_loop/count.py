# Ask user for number of cables
print("How many live cables must I avoid?")
cables_to_avoid = int(input())
# Declare a control variable
cables_avoided = 0
# Avoid cables
print()
# While loop
while(cables_avoided < cables_to_avoid):
    print("Avoiding...", end="")
    cables_avoided = cables_avoided + 1
    print(f"Done! {cables_avoided} live cable avoided!")
print("\nAll live cables have been avoided.")
