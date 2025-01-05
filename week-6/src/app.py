# Functions should do one thing!
import sys
from products import products_menu_functions
from couriers import couriers_menu_functions
from orders import orders_menu_functions
from helper_functions import print_items, check_input_int
from db import get_all

main_menu = ['0 - Exit', '1 - Products Menu', '2 - Couriers Menu', '3 - Orders Menu']

products = get_all('products')
couriers = get_all('couriers')
orders = get_all('orders')

def main_menu_function(products, couriers, orders,):
    
    print_items(main_menu)
    main_user_input = check_input_int(main_menu)

    if main_user_input == 0:
        sys.exit()
    elif main_user_input == 1:
        products_menu_functions(products)
    elif main_user_input == 2:
        couriers_menu_functions(couriers)
    elif main_user_input == 3:
        orders_menu_functions(orders)

while True:
    main_menu_function(products, couriers, orders)