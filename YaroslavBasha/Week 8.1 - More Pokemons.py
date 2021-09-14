# Code 1
def by_name(p_list=[]):
    # print('hello')
    # print(p_list)
    user_input = input('Please enter the name of the pokemon you are trying to find: ')

    if (user_input in p_list):
        print(user_input + ' does exist!')
    else:
        print('There is no pokemon with such a silly name')


pokemons = ['alpha', 'beta', 'gremlin']
by_name(pokemons)


# Code 2
def by_name(p_list=[]):
    # print('hello')
    # print(p_list)
    user_input = input('Please enter the name of the pokemon you are trying to find: ')
    pokemon_found = False
    for i in p_list:
        if (i[0] == user_input):
            pokemon_found = True
            pokemon_stored = i

    if (pokemon_found):
        print(user_input + ' does exist!')
        for x in pokemon_stored:
            print(x, end='\t')
        print()
    else:
        print('There is no pokemon with such a silly name')


p1 = ['alpha', 30, True, 'aaa']
p2 = ['beta', 50, False, 'bbb']
p3 = ['gremlin', -20, True, '']

pokemons = [p1, p2, p3]
by_name(pokemons)

# Code 3 - getting list from a file
import csv


def by_name(p_list=[]):
    # print('hello')
    # print(p_list)
    user_input = input('Please enter the name of the pokemon you are trying to find: ')
    pokemon_found = False
    for i in p_list:
        if (i[1] == user_input):
            pokemon_found = True
            pokemon_stored = i

    if (pokemon_found):
        print(user_input + ' does exist!')
        # for x in pokemon_stored:
        #     print(x, end='\t')
        # print()
        print(pokemon_stored)
    else:
        print('There is no pokemon with such a silly name')


with open('pokemons.csv', 'r') as f:
    reader = csv.reader(f)
    pokemons = list(reader)

# print(pokemons)
by_name(pokemons)