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

def create_product(name, price, connection=db_connect()):
    print('Cursor opening')
    cursor = connection.cursor()
    sql= """
        INSERT INTO products (name, price) VALUES (%s, %s)
"""
    values= (name, float(price))
    cursor.execute(sql, values)
    connection.commit()
    cursor.close()

def create_courier(name, phone, connection=db_connect()):
    print('Cursor opening')
    cursor = connection.cursor()
    sql= """
        INSERT INTO couriers (name, phone) VALUES (%s, %s)
"""
    values= (name, phone)
    cursor.execute(sql, values)
    connection.commit()
    cursor.close()

def update_product(id, name, price, connection=db_connect()):
    cursor = connection.cursor()
    if name:
        sql= """
        UPDATE products SET name = %s WHERE product_id = %s
        """
        values = (name, id)
        cursor.execute(sql, values)
    if price:
        sql= """
        UPDATE products SET price = %s WHERE product_id = %s
        """
        values = (float(price), id)
        cursor.execute(sql, values)
    connection.commit()
    cursor.close()

def update_courier(id, name, phone, connection=db_connect()):
    cursor = connection.cursor()
    if name:
        sql= """
        UPDATE couriers SET name = %s WHERE courier_id = %s
        """
        values = (name, id)
        cursor.execute(sql, values)
    if phone:
        sql= """
        UPDATE couriers SET phone = %s WHERE courier_id = %s
        """
        values = (phone, id)
        cursor.execute(sql, values)
    connection.commit()
    cursor.close()

def delete_item_db(type, id, connection=db_connect()):
    cursor = connection.cursor()
    if type == 'products':
        sql= """
            DELETE FROM products WHERE product_id = %s
    """
        values= (id)
        cursor.execute(sql, values)
    if type == 'couriers':
        sql= """
            DELETE FROM couriers WHERE courier_id = %s
    """
        values= (id)
        cursor.execute(sql, values)
    connection.commit()
    cursor.close()
