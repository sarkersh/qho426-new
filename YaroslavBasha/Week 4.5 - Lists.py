"""
Data Structures by complexity:
- primitive data types (are only built-in)
- complex data types
Data Structures by source:
- built-in
- user-defined (can only by complex)
Data Structures in Python at a glance:
- primitive data types
	int
	str
	boolean
	float
- complex data types
	list		ordered		    changeable	    allow duplicates        []
	tuple		ordered		    unchangeable	allow duplicates        ()
	set		    unordered	    changeable	    no duplicates           ()
	dictionary	unordered/	    changeable	    no duplicates           {}
			    ordered (3.7)
	user-defined data types
Python does not have arrays as built-in data type (can add as a library)
Lists however can be used as arrays
Arrays vs Lists
Arrays were first
Array are slightly more memory-efficient
Arrays are fixed in size - lists are dynamic
Arrays can only store data of the same type - lists can store different data types
Hence lists can be used as arrays - but not the other way round
"""
#################################################
# lists - collection of values
# (if you need an array, you can use list)
#################################################
# define a list: using []
fruits = []
fruits = ['apple', 'banana', 'pineapple']

print(fruits)

# adding an element to a list
fruits.append(500)
fruits.append(True)
fruits.append('cherry')
print(fruits)

# finding out its length
print('Number of elements:', len(fruits))

# it is also possible to access list elements by an index
print('The second element is', fruits[1])

# iterate over the list
for e in fruits:
    print(e)

# removing an element from a list
fruits.remove('banana')
print(fruits)

# remove the second element
del fruits[1]
print(fruits)

# remove the last element
del fruits[-1]
print(fruits)
