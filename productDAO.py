from product import Product
from psycopg2.extras import DictCursor

class ProductDAO:
    def __init__(self, conn):
        self.conn = conn

    def find_product(self, name):
        print('name', name)
        with self.conn.cursor(cursor_factory=DictCursor) as cur:
            sql = "SELECT * FROM products WHERE name = %s;"
            cur.execute(sql, (name,))
            result = cur.fetchone()
            print('find_product_res', result)
            if result:
                product = Product(
                    result['name'],
                    result['description'],
                    result['price']
                )
                product.set_id(int(result['id']))
                return product
            return None

