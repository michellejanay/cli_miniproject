from helper_functions import print_items, print_numbered_list, check_input_int, delete_item, clear_cli


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
            print_numbered_list(products)

        elif user_input == 2:
            clear_cli()
            create_input = input('What drink would you like to add? ')
            cost_input = input('How much does it cost? ')
            products.append({'name': create_input, 'price': float(cost_input)})
            clear_cli()
            print_numbered_list(products)
            print('Drink has been added')
        
        elif user_input == 3:
            clear_cli()
            print_numbered_list(products)
            update_input = check_input_int(products)
            updated_name = input('Enter the updated product name: ')
            updated_price = input('Enter the updated product price: ')
            
            if len(updated_name) > 0:
                products[update_input]['name'] = updated_name
            
            if len(updated_price) > 0:
                products[update_input]['price'] = updated_price
            
            clear_cli()
            print_numbered_list(products)
            print('Product Updated')
        
        elif user_input == 4:
            clear_cli()
            print_numbered_list(products)
            delete_input = check_input_int(products)
            products = delete_item(products, delete_input)
    