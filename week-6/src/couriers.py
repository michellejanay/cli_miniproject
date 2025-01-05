from helper_functions import print_items, print_numbered_list, check_input_int, clear_cli
from db import get_all, create_courier, update_courier, delete_item_db

def couriers_menu_functions(couriers):
    clear_cli()
    couriers_menu = ['0 - Main Menu', '1 - Print Couriers', '2 - Create New Courier', '3 - Update Existing Courier', '4 - Delete Courier']

    while True: 
        print_items(couriers_menu)
        user_input = check_input_int(couriers_menu)

        if user_input == 0:
            clear_cli()
            print('Going back to main menu...')
            return couriers
        
        elif user_input == 1:
            clear_cli()
            print_numbered_list(couriers, 'couriers')

        elif user_input == 2:
            clear_cli()
            name_input = input('Name of Courier would you like to add? ')
            phone_input = input('What is the Couriers number? ')
            create_courier(name_input, phone_input)
            clear_cli()
            print_numbered_list(get_all('couriers'), 'couriers')
            print('Courier has been added')

        elif user_input == 3:
            clear_cli()
            print_numbered_list(get_all('couriers'), 'couriers')
            update_input = input('Please select id #: ')
            updated_name = input('Enter the updated Courier Name: ')
            updated_phone = input('Enter the updated Courier Number: ')
            update_courier(update_input, updated_name, updated_phone)
            clear_cli()
            print_numbered_list(get_all('couriers'), 'couriers')
            print('Courier Updated')

        elif user_input == 4:
            clear_cli()
            print_numbered_list(get_all('couriers'), 'couriers')
            delete_input = input('Please make a selection: ')
            delete_item_db('couriers', delete_input)
            clear_cli()
            print_numbered_list(get_all('couriers'), 'couriers')
            print('Courier Deleted')