#################################################
# tuple - presenting multiple values as one
# once created, cannot be changed
#################################################

# define a tuple: using ()
person = ()
person = tuple()
person = ('James', 'Bond', 7, True, 10.99)
person = tuple(('James', 'Bond', 7, True, 10.99)) # note double (())
print(person)

# concatenate tuples
person = person + ('Casino Royale', 'Tomorrow Never Dies')
print(person)

# check if an element belongs to a tuple: using 'in'
print('Check if Casino Royale belongs to person:', 'Casino Royale' in person)
print('Check if 9 belongs to person:', 9 in person)


# iterating over a tuple:
for i in person:
    print(i)


# ***more advanced***
# storing tuples in a list
a = ('Alice', 100)
b = ('Bob', 200)
group = []
group.append(a)
group.append(b)
group.append(person)
print(group)
# group will now contain 3 elements,
# and will be list of tuples
print('Number of elements in group:', len(group))