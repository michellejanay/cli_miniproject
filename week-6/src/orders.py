from helper_functions import print_items, print_numbered_list, check_input_int, clear_cli
from db import get_all, create_order, update_order_status, update_order, delete_item_db

def orders_menu_functions(orders):
    clear_cli()
    orders_menu = ['0 - Main Menu', '1 - Print Orders', '2 - Create New Order', '3 - Update Existing Order Status', '4 - Update Existing Order', '5 - Delete Order']

    while True: 
        print_items(orders_menu)
        user_input = check_input_int(orders_menu)

        if user_input == 0:
            clear_cli()
            print('Going back to main menu...')
            return orders
        
        elif user_input == 1:
            print_numbered_list(orders, 'orders') 

        elif user_input == 2:
            clear_cli()
            name_input = input('Customer name: ')
            address_input = input('Customer address: ')
            phone_input = input('Customer phone number: ')

            print_numbered_list(get_all('products') , 'products')
            product_selection = input('Please select by number all products you would like to add, followed by a comma: ')

            print_numbered_list(get_all('couriers'), 'couriers')
            courier_selection = input('Please select a courier number: ')

            create_order(name_input, address_input, phone_input, courier_selection, product_selection)
            clear_cli()
            print_numbered_list(get_all('orders'), 'orders')
            print('Order has been added')

        elif user_input == 3:
            clear_cli()
            print_numbered_list(get_all('orders'), 'orders')
            update_input = input('Please select order number: ')
            updated_status = input('Enter the updated status: ')
            update_order_status(update_input, updated_status.upper())
            clear_cli()
            print_numbered_list(get_all('orders'), 'orders')
            print('Order status updated')

        elif user_input == 4:
            clear_cli()
            print_numbered_list(get_all('orders'), 'orders')
            update_input = input('Please make a selection: ')
            to_update = {'customer_name': '', 'customer_address':'', 'customer_phone': '', 'courier_selection': '', 'items': ''}

            for key,value in to_update.items(): 
                to_be_updated = input(f'Please put updated value for {key}. If no update, press enter: ')

                if len(to_be_updated) > 0:
                    to_update[key] = to_be_updated

            update_order(update_input, to_update)
            clear_cli()
            print_numbered_list(get_all('orders'), 'orders')
            print('Order updated')

        elif user_input == 5:
            print_numbered_list(get_all('orders'), 'orders')
            delete_input = input('Please make a selection: ')
            delete_item_db('orders', delete_input)
            clear_cli()
            print_numbered_list(get_all('orders'), 'orders')
            print('Order Deleted')