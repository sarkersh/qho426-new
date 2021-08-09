user_input=int(input("Please enter a whole number: "))
if (user_input % 2 == 0):
    print(f"\nThe number {user_input} is an even number.")
else:
    print("\nThe number {} is an odd number.".format(user_input))