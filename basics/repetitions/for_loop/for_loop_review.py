"""
Different kinds of loop:
1.	Count-controlled for loop (Three-expression for loop)
The header of this kind of for loop consists of a three-parameter loop control expression. Generally it has the form:
 (A; Z; I) A is the initialization part, Z determines a termination expression, where the loop variable is
 incremented or decremented. But this kind of loop nit implemented in python.
2.	Numeric Ranges
This kind of loop is a simplification of previous kind. It’s a counting or enumerating loop. Starting with a start value
 and counting up to an end value, like for i = 1 to 100 Python doesn’t use this either.
3.	Vectorized for loops
They behave as if all iterations are executed in parallel. That is, for example, all expression on the right side of
assignment statements get evaluated before the assignments.
4.	Iterator-based for loop
Finally, we come to the one use by Python. This kind of for loop iterates over an enumeration of a set of items. It is
usually characterized by the use of an implicit or explicit iterator. In each iteration step a loop variable is set to
a value in a sequence or other data collection. This kind of for loop is known in most Unix and Linux shells and it is
the one which is implemented in Python.
Syntax of the For Loop:
As we mentioned earlier, the Python for loop is an iterator based for loop. It steps through the items of
lists, tuples, strings, the keys of dictionaries and other iterables. The Python for loop starts with the keyword "for"
followed by an arbitrary variable name, which will hold the values of the following sequence object,
which is stepped through. The general syntax looks like this:
for in : else:
The items of the sequence object are assigned one after the other to the loop variable; to be precise the variable
points to the items. For each item the loop body is executed.
Example of a simple for loop in Python:

"""
languages = ["C", "C++", "Perl", "Python"]
for language in languages:
    print(language)

edibles = ["bacon", "spam", "eggs", "nuts"]
for food in edibles:
    if food == "spam":
        print("No more spam please!")
        break
    print("Great, delicious " + food)
else:
    print("I am so glad: No spam!")
print("Finally, I finished stuffing myself")

edibles = ["bacon", "spam", "eggs", "nuts"]
for food in edibles:
    if food == "spam":
        print("No more spam please!")
        continue
    print("Great, delicious " + food)
else:
    print("I am so glad: No spam!")
print("Finally, I finished stuffing myself")
# The range() Function:
# The built-in function range() is the right function to iterate over a sequence of numbers.
# It generates an iterator of arithmetic progressions: Example: range(5) Output: range(0,5) , mean number of 0 to 4.
# We can use in a for loop and it is meant by this:
for i in range(5):
    print(i)
# range(n) generates an iterator to progress the integer numbers starting with 0 and ending with (n -1).
# To produce the list with these numbers, we have to cast range() with the list(), as we do in the following example
# list(range(10) Output: [0,1,2,3,4,5,6,7,8,9]
# range() can also be called with two arguments: range(begin, end)
# The above call produces the list iterator of numbers starting with begin (inclusive) and ending with one less than
# the number end. Example: range(4, 10) Output: range(4, 10)
# list(range(4, 10)) Output: [4, 5, 6, 7, 8, 9] So far the increment of range() has been 1. We can specify a different
# increment with a third argument. The increment is called the step. It can be both negative or positive, but no zero:
# range(begin, end, step) Example with step: list(range(4, 50, 5)) So start with 4 , end with 49 and increment by 5
# That means 4 then 9 as 4+5=9, 14 as 9+5=14 and so far on.....till 50 means 49.
# It can be backward as well: list(range(42, -12, -7) Output will be: [42,35(42-7),28(35-7),21(28-7)....-7 ]
# The range() function is especially useful in combination with the for loop, as we can see in the following example.
# The range() function supplies the numbers from 1 to 100 for the for loop to calculate the sum of these numbers:
n = 100
sum = 0
for counter in range(1, n+1):
    sum = sum + counter
print("Sum of 1 until {:d}: {:d}".format(n, sum))
# Calculation of the Pythagorean Numbers
# Definition is very simple: Three integers satisfying a2+b2=c2 are called Pythagorean numbers.
# The following program calculates all pythagorean numbers less than a maximal number.
# Remark: We have to import the math module to be able to calculate the square root of a number.
from math import sqrt
n = int(input("Maximal Number? "))
for a in range (1, n+1):
    for b in range(a, n):
        c_square = a**2+b**2
        c = int(sqrt(c_square))
        if ((c_square - c**2) == 0):
            print(a, b, c)




















