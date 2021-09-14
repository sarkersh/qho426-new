for count in range(1):
    print("#########")
    print("#       #")
    print("# O   O #")
    print("|   V   |")
    print("|  ---  |")
    print("|_______|")
for count in range(0, 10, 1): # (0, 10, 5) where these represent the start, stop and step of the sequence.
    print("#########")
    print("#       #")
    print("# O   O #")
    print("|   V   |")
    print("|  ---  |")
    print("|_______|")
# Ask user for number of mountains
print("How many mountains should I display?")
m = int(input()) # (m = mountains)
# Display mountains
print("\nDisplaying...")
for mountains in range(m):
    print(""" 
            __
          /  \\_  
         /^    \\
        /  ^    \\_
      _/ ^ ^     ^\\
     /  ^     ^    \\   
    
    """)
print("Done!")










