from product import Product
from psycopg2.extras import DictCursor

class ProductDAO():
    def __init__(self, conn):
        self.conn = conn

    def find_product(conn, name):
        print('name', name)
        with conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute("SELECT * FROM products WHERE name = %s;", (name,))
            result = cur.fetchone()
            print('find_product_res', result)
            if result:
                return Product(**result)
        return None

