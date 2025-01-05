import psycopg2 as psycopg
import os
from dotenv import load_dotenv

load_dotenv()
host_name = os.environ.get("POSTGRES_HOST")
database_name = os.environ.get("POSTGRES_DB")
user_name = os.environ.get("POSTGRES_USER")
user_password = os.environ.get("POSTGRES_PASSWORD")

def db_connect():
    try: 
        with psycopg.connect(f"""
        host={host_name}
        dbname={database_name}
        user={user_name}
        password={user_password}
        """) as connection:
            return connection
    except Exception as ex:
        print('Failed to:', ex)


def get_all(type, connection=db_connect()):
    cursor = connection.cursor()
    sql=f"""
        SELECT * FROM {type} ORDER BY {type[:-1]}_id
    """
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    return rows

def get_headers(type, connection=db_connect()):
    cursor = connection.cursor()
    sql=f"""
        SELECT column_name
        FROM information_schema.columns
        WHERE table_name = '{type}'
        ORDER BY ordinal_position;
    """
    cursor.execute(sql)
    column_names_tuple = cursor.fetchall()
    column_names = []
    for name in column_names_tuple:
        column_names.append(name[0])
    cursor.close()
    return column_names

def create_product(name, price, connection=db_connect()):
    print('Cursor opening')
    cursor = connection.cursor()
    sql= f"""
        INSERT INTO products (name, price) VALUES ('{name}', {float(price)})
"""
    cursor.execute(sql)
    connection.commit()
    cursor.close()

def create_courier(name, phone, connection=db_connect()):
    cursor = connection.cursor()
    sql= f"""
        INSERT INTO couriers (name, phone) VALUES ('{name}', '{phone}')
"""
    cursor.execute(sql)
    connection.commit()
    cursor.close()

def update_product(id, name, price, connection=db_connect()):
    cursor = connection.cursor()
    if name:
        sql= f"""
        UPDATE products SET name = '{name}' WHERE product_id = {id}
        """
        cursor.execute(sql)
    if price:
        sql= f"""
        UPDATE products SET price = {float(price)} WHERE product_id = {id}
        """
        cursor.execute(sql)
    connection.commit()
    cursor.close()

def update_courier(id, name, phone, connection=db_connect()):
    cursor = connection.cursor()
    if name:
        sql= f"""
        UPDATE couriers SET name = '{name}' WHERE courier_id = {id}
        """
        cursor.execute(sql)
    if phone:
        sql= f"""
        UPDATE couriers SET phone = '{phone}' WHERE courier_id = {id}
        """
        cursor.execute(sql)
    connection.commit()
    cursor.close()

def delete_item_db(type, id, connection=db_connect()):
    cursor = connection.cursor()
    if type == 'products':
        sql= f"""
            DELETE FROM products WHERE product_id = {id}
    """
        cursor.execute(sql)
    if type == 'couriers':
        sql= f"""
            DELETE FROM couriers WHERE courier_id = {id}
    """
        cursor.execute(sql)
    if type == 'orders':
        sql= f"""
            DELETE FROM orders WHERE order_id = {id}
    """
        cursor.execute(sql)
    connection.commit()
    cursor.close()

def create_order(customer_name, customer_address, customer_phone, courier_selection, items, connection=db_connect()):
    cursor = connection.cursor()
    sql= f"""
        INSERT INTO orders (customer_name, customer_address, customer_phone, courier, order_status, items) VALUES ('{customer_name}', '{customer_address}', '{customer_phone}', '{courier_selection}', 'PREPARING', '{items}')
"""
    cursor.execute(sql)
    connection.commit()
    cursor.close()

def update_order_status(id, new_status, connection=db_connect()):
    cursor = connection.cursor()
    if new_status:
        sql= f"""
        UPDATE orders SET order_status = '{new_status}' WHERE order_id = {id}
        """
        cursor.execute(sql)
    connection.commit()
    cursor.close()

def update_order(id, updated_order, connection=db_connect()):
    cursor = connection.cursor()
    for key, value in updated_order.items():
        if len(value) > 0:
            sql= f"""
        UPDATE orders SET {key} = '{value}' WHERE order_id = {id}
        """
        cursor.execute(sql)
    connection.commit()
    cursor.close()