# Activity 1: Nested Loop
"""
Loops can be nested.  That is one loop can be placed inside another.
When this is done it results in the inner loop being executed for each iteration of the outer loop.
[Explanation]
Let us consider a simple example where we wish to display the digits 0-9 on a single line.
We can do this using a single loop as follows:
for number in range(0, 10, 1):
    print(number, "|", end="")
Out put: 0 |1 |2 |3 |4 |5 |6 |7 |8 |9 |
Note, that all the numbers are displaying on the same line. This is because
we have overridden the default behaviour of the print function.
By default the print function adds a new line (\n) to the end of a line.
However, by using end="" we have specified that an empty string ("") should be added to the end of the
printed line instead of a new line (\n).
########################################################################################################################
for count in range(0, 3, 1):
    for number in range(0, 10, 1):
        print(number, "|", end="")

Output: 0 |1 |2 |3 |4 |5 |6 |7 |8 |9 |0 |1 |2 |3 |4 |5 |6 |7 |8 |9 |0 |1 |2 |3 |4 |5 |6 |7 |8 |9 |

Note that all the numbers are displayed on the same line as we have not included an instruction in the program to
display to the next line. Assume our intention was to display each set of digits on a new line. This means on each
iteration of the outer loop we will need to move to a new line. Our code would therefore look as follows:
for count in range(0, 3, 1):
    for number in range(0, 10, 1):
        print(number, "|", end="")
    print()
In the above code, the last print statement will cause a new line (\n) character to be displayed after the inner loop
has completed execution. The resulting output would look as follows:
Output:
0 |1 |2 |3 |4 |5 |6 |7 |8 |9 |
0 |1 |2 |3 |4 |5 |6 |7 |8 |9 |
0 |1 |2 |3 |4 |5 |6 |7 |8 |9 |
https://learn.solent.ac.uk/pluginfile.php/2793907/mod_page/content/1/nested-loop.png
"""
########################################################################################################################
print("How many rows should I have?")
rows = int(input())
print("How many columns should I have?")
cols = int(input())

for row in range(0,rows,1):
    for col in range(0,cols,1):
        print(":-)", end="")
    print()



















