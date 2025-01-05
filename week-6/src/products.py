from helper_functions import print_items, print_numbered_list, check_input_int, clear_cli
from db import get_all, create_product, update_product, delete_item_db


def products_menu_functions(products):
    clear_cli()
    products_menu = ['0 - Main Menu', '1 - Print Products', '2 - Create New Product', '3 - Update Existing Products', '4 - Delete Product']
     
    while True: 
        print_items(products_menu)

        user_input = check_input_int(products_menu)

        if user_input == 0:
            clear_cli()
            print('Going back to main menu...')
            return products
        
        elif user_input == 1:
            clear_cli()
            print_numbered_list(products, 'products')

        elif user_input == 2:
            clear_cli()
            create_input = input('What drink would you like to add? ')
            cost_input = input('How much does it cost? ')
            create_product(create_input, cost_input)
            clear_cli()
            print_numbered_list(get_all( 'products'), 'products')
            print('Drink has been added')
        
        elif user_input == 3:
            clear_cli()
            print_numbered_list(get_all('products'), 'products')
            update_input = input('Please select id #: ')
            updated_name = input('Enter the updated product name: ')
            updated_price = input('Enter the updated product price: ')    
            update_product(update_input, updated_name, updated_price)
            clear_cli()
            print_numbered_list(get_all('products'), 'products')
            print('Product Updated')
        
        elif user_input == 4:
            clear_cli()
            print_numbered_list(get_all('products'), 'products')
            delete_input = input('Please make a selection: ')
            delete_item_db('products', delete_input)
            print_numbered_list(get_all('products'), 'products')
            print('Product Deleted')
    