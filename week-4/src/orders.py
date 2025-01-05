from helper_functions import print_items, print_numbered_list, check_input_int, delete_item, clear_cli

def create_order(name, address, phone, courier, status, items):
    order = {
        'customer_name': name,
        'customer_address': address,
        'customer_phone': phone,
        'courier': courier,
        'order_status': status,
        'items': items
    }
    return order

def orders_menu_functions(orders, products, couriers):
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
            print_numbered_list(orders) 

        elif user_input == 2:
            clear_cli()
            name_input = input('Customer name: ')
            address_input = input('Customer address: ')
            phone_input = input('Customer phone number: ')

            print_numbered_list(products)
            product_selection = input('Please select by number all products you would like to add, followed by a comma: ')

            print_numbered_list(couriers)
            courier_selection = check_input_int(couriers)

            orders.append(create_order(name_input, address_input, phone_input, courier_selection, 'preparing', product_selection))
            clear_cli()
            print_numbered_list(orders)
            print('Order has been added')

        elif user_input == 3:
            clear_cli()
            print_numbered_list(orders)
            update_input = check_input_int(orders)
            updated_status = input('Enter the updated status: ')
            
            if len(updated_status) > 0:
                orders[update_input]['order_status'] = updated_status
            
            clear_cli()
            print_numbered_list(orders)
            print('Order status updated')

        elif user_input == 4:
            clear_cli()
            print_numbered_list(orders)
            update_input = check_input_int(orders)

            for key in orders[update_input]: 
                to_be_updated = input(f'Please put updated value for {key}. If no update, press enter: ')

                if len(to_be_updated) > 0:
                    orders[update_input][key] = to_be_updated
            
            clear_cli()
            print_numbered_list(orders)
            print('Order updated')

        elif user_input == 5:
            print_numbered_list(orders)
            delete_input = check_input_int(orders)
            delete_item(orders, delete_input)
            clear_cli()
            print_numbered_list(orders)
            print('Order Deleted')