from tabulate import tabulate
import os

def clear_cli():
    os.system('cls' if os.name=='nt' else 'clear')

def print_items(menu):
    for item in menu:
        print(item)


def print_numbered_list(list):
    print(tabulate(list, headers="keys", tablefmt="pretty", showindex='always'))


def delete_item(list, delete_index):
    del list[delete_index]
    print_numbered_list(list)
    print('Item deleted')
    return list


def check_input_int(menu):
    menu_length = (range(len(menu)))
    try:
        main_user_input = int(input('Please make a selection: '))
        if (main_user_input not in menu_length):
            raise ValueError
        return main_user_input
    except ValueError:
        print('Value error raised in except block')
        print(f'Please make an input between 0-{len(menu_length) - 1}')
