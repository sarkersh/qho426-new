"""
12 - Built In Functions # Activity 1: ASCII Value
1. Code reuse :  A block of code can be reused multiple times by the program or even other programs
2. Abstraction: A function can be used without knowing the details of how it works.
In Python, as well as many other languages, we generally have two categories of functions -
built-in functions and user-defined functions.
    * Built-in functions are functions that are part of the standard libraries of the programming language.
    Python functions such as print and input are built-in functions.
    * User-defined functions are functions written to address certain requirements.
    They can improve code reuse and extend capabilities beyond that provided by the standard libraries.
    We have already encountered some built-in functions including print, input, format, range and
those for converting data types (int, float, str).  Python provides many built-in functions for common tasks and
our convenience.  A list of these can be found in the table below:
abs()	delattr()	hash()	memoryview()	set()   all()	dict()	help()	min()	setattr()
any()	dir()	hex()	next()	slice()     ascii()	divmod()	id()	object()	sorted()
bin()	enumerate()	input()	oct()	staticmethod()  bool()	eval()	int()	open()	str()
breakpoint()	exec()	isinstance()	ord()	sum()   bytearray()	filter()	issubclass()	pow()	super()
bytes()	float()	iter()	print()	tuple()     callable()     format()     len()   property()  type()  chr()   frozenset()
list()	range()	vars()  classmethod()	getattr()   locals()       repr()   zip()   compile()      globals()
map()   reversed()  __import__()    complex()	hasattr()   max()   round()
https://learn.solent.ac.uk/pluginfile.php/2793910/mod_page/content/4/ascii-table.png
"""
print("Program Started!")
print("Please enter a standard character:")
character = input()
if(len(character) == 1):
    print( f"The ASCII code for {character} is {ord(character)}.")
else:
    print("A single character was expected.")
print("Program Ended!")


