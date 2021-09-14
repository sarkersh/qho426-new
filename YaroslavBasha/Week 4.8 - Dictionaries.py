####################################################
# Dictionaries
#
# - store key:value pairs
# - created using {curly brackets}
# - are unordered/ordered (depending on Python version)
# - mutable (can be changed)
# - each key can only be stored once
####################################################

# to declare dictionary - use {}
my_dict = {}

# to declare and initialise:
my_dict = {'Name':'Yaroslav', 'Job':'--', 'Subject':'--'}

# print it
print(my_dict)

# duplicate keys are ignored
# (the earlier one is removed, the later one is remembered)
my_dict = {'Name':'Yaroslav', 'Job':'--', 'Subject':'--', 'Job':'Tutor', 'Subject':'Data Analysis'}
print(my_dict)

# getting number of elements in a dictionary
print('There are', len(my_dict), 'entries in the dictionary')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# adding entires into a dictionary
print(my_dict)
my_dict['Location'] = 'Manchester'
my_dict['Experience'] = 20
print(my_dict)
print('There are', len(my_dict), 'entries in the dictionary')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# accessing a single element from a dictionary
# very similar to lists/arrays
my_dict['Name']
print('Name is', my_dict['Name'])
my_dict['Job'] = 'Senior Tutor'
print(my_dict)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# iterating over all elements - generic
for k in my_dict:
    print(k, '\t:', my_dict[k])
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# iterating over all elements - dictionaries only
for k,v in my_dict.items():
    print('The key is {} and the value is {}'.format(k,v))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# removing elements from a dictionary
del my_dict['Location']
print(my_dict)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')