#################################################
# set
# the same as set in math
# each element can only be stored once, i.e
# {A,B,C} + {B,C,D} = {A,B,C,D}
# unordered, ignore duplicates
#################################################

# define a set: using {}
one_set = {}
one_set = {'A','B','C'}
print(one_set)

# duplicates are ignored
one_set = {'A', 'A', 'B', 'B', 'B', 'C'}
print(one_set)


# iterate over
for i in one_set:
    print(i)


# length of a set
print('Number of elements in this set:', len(one_set))

# adding elements to a set
one_set.add('D')
one_set.add('D')
one_set.add('E')
one_set.add('E')
print(one_set)


# converting set to a list
mylist = []
# iterate over
for i in one_set:
    #print(i)
    mylist.append(i)
print('List:', mylist)