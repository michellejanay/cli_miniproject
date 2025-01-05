from tabulate import tabulate
from db import get_all,get_headers
import os

def clear_cli():
    os.system('cls' if os.name=='nt' else 'clear')

def print_items(menu):
    for item in menu:
        print(item)


def print_numbered_list(list, type):
    print(tabulate(list, headers=get_headers(type), tablefmt="pretty"))


def check_input_int(menu):
    menu_length = (range(len(menu)))
    try:
        main_user_input = int(input('Please make a selection: '))
        if (main_user_input not in menu_length):
            raise ValueError
        return main_user_input
    except ValueError:
        print('ValueError raised in except block')
        print(f'Please make an input between 0-{len(menu_length) - 1}')