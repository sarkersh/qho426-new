"""
nested loop = The "inner loop" will finish all of it's iterations before finishing one iteration of the "outer loop"
outer loop for rows
and inner loop columns

"""
rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()

"""
Output:
How many rows?: 5
How many columns?: 7
Enter a symbol to use: @
@@@@@@@
@@@@@@@
@@@@@@@
@@@@@@@
@@@@@@@

"""











