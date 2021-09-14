# Ask user for sequence and marker
print("Please enter a sequence:")
sequence = input()
print("Please enter the character for the marker:")
marker = input()
# Find markers position
marker1_position = -1
marker2_position = -1
for position in range(0,len(sequence), 1):
    letter = sequence[position]
    if (letter == marker):
        if(marker1_position == -1):
            marker1_position = position
        else:
            marker2_position = position
# Display result:
print(f"The distance between the markers is {marker2_position - marker1_position -1}.")
# Alternative solution where we remember whether we are counting.  Also reduces nesting:
# Ask user for sequence and marker
print("Please enter a sequence:")
sequence = input()
print("Please enter the character for the marker:")
marker = input()
# Find markers
is_counting = False
count = 0
for character in sequence:
    if (is_counting == False and character == marker):
        print("Found first marker")
        is_counting = True
    elif (is_counting == True and character == marker):
        print("Found last marker")
    elif (is_counting):
        count += 1

# Display result
print(f"The distance between the markers is {count}")