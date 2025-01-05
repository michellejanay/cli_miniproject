from helper_functions import print_items, print_numbered_list, check_input_int, delete_item, clear_cli

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
            print_numbered_list(couriers)

        elif user_input == 2:
            clear_cli()
            name_input = input('Name of Courier would you like to add? ')
            phone_input = input('What is the Couriers number? ')
            couriers.append({'name': name_input, 'phone': phone_input})
            clear_cli()
            print_numbered_list(couriers)
            print('Courier has been added')

        elif user_input == 3:
            clear_cli()
            print_numbered_list(couriers)
            update_input = check_input_int(couriers)
            updated_name = input('Enter the updated Courier Name: ')
            updated_phone = input('Enter the updated Courier Number: ')
            
            if len(updated_name) > 0:
                couriers[update_input]['name'] = updated_name
            
            if len(updated_phone) > 0:
                couriers[update_input]['phone'] = updated_phone
            
            clear_cli()
            print_numbered_list(couriers)
            print('Courier Updated')

        elif user_input == 4:
            clear_cli()
            print_numbered_list(couriers)
            delete_input = check_input_int(couriers)
            couriers = delete_item(couriers, delete_input)
            clear_cli()
            print_numbered_list(couriers)
            print('Courier deleted')