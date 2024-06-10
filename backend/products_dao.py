from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()

    query = ("select products.product_id, products.product_name, products.units_id, products.price_per_unit, units.unit_name from products inner join units on products.units_id=units.units_id")

    cursor.execute(query)
    response=[]
    for (product_id, product_name, units_id, price_per_unit, unit_name) in cursor:
        response.append(
            {
                'product_id' : product_name,
                'product_name' : product_name,
                'units_id' : units_id,
                'price_per_unit' : price_per_unit,
                'unit_name' : unit_name

            }
        )


    return response

def insert_new_products(connection, products):
    cursor = connection.cursor()
    query = ("INSERT INTO products "
             "(product_name, units_id, price_per_unit)"
             "VALUES (%s, %s, %s)")
    data = (products['product_name'], products['units_id'], products['price_per_unit'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid


def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid


if __name__ == '__main__':
    connection = get_sql_connection()
    print(delete_product(connection, 12))