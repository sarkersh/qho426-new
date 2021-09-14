def print_separator():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# main storage
fruits = {'apples':0, 'bananas':0, 'cherries':0}


# MENU: list items
def list_items():
    print('Listing items...\nFruit\tQty')
    for i,v in fruits.items():
        print('{}\t{}'.format(i, v))


# MENU: add item
def add_item():
    print('Adding item...')
    c = 0
    for i in fruits:
        print(c, ':', i)
        c = c+1
    items = list(fruits)
    #print(items[1])
    u = int(input('Which fruit would you like to add: '))
    #print(u)
    #print(items[u])
    #print(fruits[items[u]])
    fruits[items[u]] = fruits[items[u]] + 1
    #print(fruits[items[u]])
    list_items()


# MENU: add item
def remove_item():
    print('Removing item...')


# simply print main menu and get user input
def menu():
    print_separator()
    print('Main Menu')
    print_separator()
    # print('1 - List items')
    # print('2 - Add items')
    # print('0 - Exit')

    menu_options = {1:'List items', 2:'Add item', 3:'Remove item', 0:'Exit'}

    # iterating over dictionaries only
    for i,v in menu_options.items():
        print('{}\t{}'.format(i, v))

    print_separator()
    choice = int(input('What would you like to do now: '))
    # if (choice in menu_options):
    #     print('yes')
    # else:
    #     print('no')
    while (choice not in menu_options):
        print('Wrong choice!')
        choice = int(input('What would you like to do now: '))
    #return user's choice
    return choice


# main execution loop
def run():
    user_choice = menu()
    while (user_choice != 0):
        if (user_choice == 1):
            list_items()
        if (user_choice == 2):
            add_item()
        if (user_choice == 3):
            remove_item()
        # ask user again
        user_choice = menu()
    print_separator()
    print('Bye!')
    print_separator()

# execute the program
run()


# HOMEWORK 1:
# Complete function remove_item()
# HOMEWORK 2:
# Add two more menu items which will allow to edit content of items (e.g. add strawberry and remove cherry)