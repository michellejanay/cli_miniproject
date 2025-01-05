import os
menu = ['0 - Exit', '1 - Print Products', '2 - Create New Product', '3 - Update Existing Products', '4 - Delete Product']

products = ['White Coffee', 'Black Coffee', 'Cappuccino', 'Latte', 'Mocha']

def print_menu():
    for item in menu:
        print(item)

def print_products():
    for product in products:
        print(f'{products.index(product) + 1} - {product}')

print_menu()

user_input = int(input('Please make a selection: '))

if (user_input < 0) or (user_input > 4):
    print_menu()
    print('Please make an input between 0-4')
    user_input = int(input('Please make a selection: '))

if user_input == 0:
    exit()
elif user_input == 1:
    os.system('cls')
    print_products()
    drink_input = int(input('Please make a selection: '))
    if drink_input == 0:
        os.system('cls')
        print_menu()
        user_input = int(input('Please make a selection: '))
    elif drink_input == 1:
        print(products[0])
    elif drink_input == 2:
        print(products[1])
    elif drink_input == 3:
        print(products[2])
    elif drink_input == 4:
        print(products[3])
    elif drink_input == 5:
        print(products[4])
elif user_input == 2:
    os.system('cls')
    create_input = input('What drink would you like to add? ')
    products.append(create_input)
    print('Drink has been added')
    print_products()
elif user_input == 3:
    os.system('cls')
    print_products()
    update_input = int(input('Enter the number of the product you would like to update '))
    if (update_input < 1) or (update_input > 5):
        print('Please make a selection from 1-5')
        update_input = int(input('Enter the number of the produt you would like to update '))
    else:
        updated_product = input('Enter the updated product ')
        os.system('cls')
        products[update_input - 1] = updated_product
        print('Product Updated')
        print_products()
elif user_input == 4:
    os.system('cls')
    print_products()
    delete_input = int(input('Enter the number of the product you would like to delete '))
    if (delete_input < 1) or (delete_input > 5):
        print('Please make a selection from 1-5')
        delete_input = int(input('Enter the number of the produt you would like to delete '))
    else:
        products.pop(delete_input - 1)
        print('Product deleted')
        print_products()