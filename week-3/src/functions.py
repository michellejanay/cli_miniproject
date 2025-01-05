import os
def view_items(filename):
    with open(f'{filename}', 'r') as file:
        items = []
        for line in file.readlines():
            items.append(line.rstrip())
        return items

def append_item(filename, to_append):
    with open(f'{filename}', 'a+') as file:
        file.write(f'\n{to_append}')

# def update_item(filename, index, to_update):
    # with open (filename, 'r+') as file:
    #     for line in file.readlines():
        

def print_items(items):
    for item in items:
        print(item)

def print_numbered_list(list):
    for item in list:
        print(f'{list.index(item) + 1} - {item}')



def menu_functions(menu,data_file):
    print_items(menu)
    user_input = int(input('Please make a selection: '))

    if (user_input < 0) or (user_input > 4):
        print_items(menu)
        print('Please make an input between 0-4')
        user_input = int(input('Please make a selection: '))
    
    if user_input == 0:
        print('Going back to main menu')

    elif user_input == 1:
        os.system('cls')
        print_numbered_list(view_items(data_file))
        print_input = int(input('Please make a selection: '))
        if print_input == 0:
            os.system('cls')
            print_items(menu)
            user_input = int(input('Please make a selection: '))
        elif print_input in (range(len(view_items(data_file)))):
            items = view_items(data_file)
            print(items[print_input - 1])
    elif user_input == 2:
        if data_file == '../data/products.txt':
            os.system('cls')
            create_input = input('What/Who would you like to add? ')
            append_item(data_file, create_input)
            print_numbered_list(view_items(data_file))
            print('Drink has been added')
    elif user_input == 3:
        os.system('cls')
        # print_numbered_list(products)
        # update_item_or_order(products_menu)
    elif user_input == 4:
        os.system('cls')
        # print_numbered_list(products)
        # delete_item(products)