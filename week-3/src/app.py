# Functions should do one thing!
import os
import functions
main_menu = ['0 - Exit', '1 - Products Menu', '2 - Orders Menu', '3 - Couriers Menu']
products_menu = ['0 - Main Menu', '1 - Print Products', '2 - Create New Product', '3 - Update Existing Products', '4 - Delete Product']
orders_menu = ['0 - Main Menu', '1 - Print Orders', '2 - Create New Order', '3 - Update Existing Order Status', '4 - Delete Order']
couriers_menu = ['0 - Main Menu', '1 - Print Couriers', '2 - Create New Courier', '3 - Update Existing Courier', '4 - Delete Courier']
products = ['White Coffee', 'Black Coffee', 'Cappuccino', 'Latte', 'Mocha']
orders = [{'customer_name': 'michelle', 'customer_address': 'my address', 'customer_phone': 'my phone number', 'order_status': 'received'}]
is_open = True

def print_items(items):
    for item in items:
        print(item)

def print_numbered_list(list):
    for item in list:
        print(f'{list.index(item) + 1} - {item}')

def create_order(name, address, phone, status):
    order = {
        'customer_name': name,
        'customer_address': address,
        'customer_phone': phone,
        'status': status
    }
    orders.append(order)

def delete_item(list):
    delete_input = int(input('Enter the number of the item you would like to delete: '))
    if (delete_input < 1) or (delete_input > len(list) + 1):
            print(f'Please make a selection from 1-{len(list) + 1}')
            delete_input = int(input('Enter the number of the item you would like to delete: '))
    if (list == products):
        products.pop(delete_input - 1)
        print_numbered_list(products)
        print('Product deleted')
    if (list == orders):
        orders.pop(delete_input - 1)
        print_numbered_list(orders)
        print('Order deleted')


def update_item_or_order(menu):
    update_input = int(input('Enter the number of the you would like to update: '))
    if (update_input < 1) or (update_input > 5):
        print('Please make a selection from 1-5')
        update_input = int(input('Enter the number of the you would like to update: '))
    if(menu == products_menu):
        updated_product = input('Enter the updated product: ')
        os.system('cls')
        products[update_input - 1] = updated_product
        print_numbered_list(products)
        print('Product Updated')
    if(menu == orders_menu):
        updated_status = input('Enter the updated status: ')
        orders[update_input - 1]['status'] = updated_status
    

def products_menu_functions():
    functions.menu_functions(products_menu, '../data/products.txt')
#     print_items(products_menu)
#     user_input = int(input('Please make a selection: '))
# # when user selects print products, let them know 0 is to go back to previous menu
#     if (user_input < 0) or (user_input > 4):
#         print_items(products_menu)
#         print('Please make an input between 0-4')
#         user_input = int(input('Please make a selection: '))

#     if user_input == 0:
#         main_menu_function()
#     elif user_input == 1:
#         os.system('cls')
#         print_numbered_list(functions.view_items('../data/products.txt'))
#         drink_input = int(input('Please make a selection: '))
#         if drink_input == 0:
#             os.system('cls')
#             print_items(products_menu)
#             user_input = int(input('Please fix me: '))
#         # elif drink_input == 1:
#         #     print(products[0])
#         # elif drink_input == 2:
#         #     print(products[1])
#         # elif drink_input == 3:
#         #     print(products[2])
#         # elif drink_input == 4:
#         #     print(products[3])
#         # elif drink_input == 5:
#         #     print(products[4])
#     elif user_input == 2:
#         os.system('cls')
#         create_input = input('What drink would you like to add? ')
#         functions.append_item('../data/products.txt', create_input)
#         print_numbered_list(functions.view_items('../data/products.txt'))
#         print('Drink has been added')
#     elif user_input == 3:
#         os.system('cls')
#         print_numbered_list(products)
#         update_item_or_order(products_menu)
#     elif user_input == 4:
#         os.system('cls')
#         print_numbered_list(products)
#         delete_item(products)

def orders_menu_functions():
    print_items(orders_menu)
    user_input = int(input('Please make a selection: '))

    if (user_input < 0) or (user_input > 4):
        print_items(orders_menu)
        print('Please make an input between 0-4')
        user_input = int(input('Please make a selection: '))

    if user_input == 0:
        main_menu_function()
    elif user_input == 1:
        os.system('cls')
        print_items(orders)
    elif user_input == 2:
        os.system('cls')
        name_input = input('Customer name: ')
        address_input = input('Customer address: ')
        phone_input = input('Customer phone number: ')
        status_input = input('Order Status: ')
        create_order(name_input, address_input, phone_input, status_input)
        print('Order has been added')
        print_items(orders)
    elif user_input == 3:
        os.system('cls')
        print_numbered_list(orders)
        update_item_or_order(orders_menu)
        print_items(orders)
        print('Order Updated')
    elif user_input == 4:
        os.system('cls')
        print_numbered_list(orders)
        delete_item(orders)
        print_numbered_list(orders)
        if (len(orders) == 0):
            print('No orders at this time')

def main_menu_function():
    print_items(main_menu)
    user_input = int(input('Please make a selection: '))
    if (user_input < 0) or (user_input > len(main_menu) + 1):
        print_items(main_menu)
        print('Please make an input between 0-2')
        user_input = int(input('Please make a selection: '))

    if user_input == 0:
        exit()
    elif user_input == 1:
        products_menu_functions()
    elif user_input == 2:
        orders_menu_functions()
    elif user_input == 3:
        print_items(couriers_menu)

while is_open:
    main_menu_function()