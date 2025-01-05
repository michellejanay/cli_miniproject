# Functions should do one thing!
import sys
from products import products_menu_functions
from couriers import couriers_menu_functions
from orders import orders_menu_functions
from helper_functions import print_items, check_input_int
from persisting import view_items, save_data

main_menu = ['0 - Exit', '1 - Products Menu', '2 - Couriers Menu', '3 - Orders Menu']

products = view_items('../data/products.csv')
couriers = view_items('../data/couriers.csv')
orders = view_items('../data/orders.csv')

def main_menu_function(products, couriers, orders,):
    
    print_items(main_menu)
    main_user_input = check_input_int(main_menu)

    if main_user_input == 0:
        save_data('../data/products.csv', products, ['name', 'price'])
        save_data('../data/couriers.csv', couriers, ['name', 'phone'])
        save_data('../data/orders.csv', orders, ['customer_name', 'customer_address', 'customer_phone', 'courier', 'order_status', 'items'])
        sys.exit()
    elif main_user_input == 1:
        products = products_menu_functions(products)
    elif main_user_input == 2:
        couriers = couriers_menu_functions(couriers)
    elif main_user_input == 3:
        orders = orders_menu_functions(orders, products, couriers)

while True:
    main_menu_function(products, couriers, orders)