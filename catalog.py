import psycopg2
from productDAO import ProductDAO
"""
try:
    # пытаемся подключиться к базе данных
    conn = psycopg2.connect(dbname='hexlet', user='ivan',  host='/var/run/postgresql')
    #conn = psycopg2.connect(dbname='ivan', user='u0_a440',  host='/data/data/com.termux/files/usr/tmp')
except:
    # в случае сбоя подключения будет выведено сообщение в STDOUT
    print('Can`t establish connection to database')"""
    
class Catalog:
    def __init__(self, conn):
        self.conn = conn
    
    def get_product(self, name):
        dao = ProductDAO(self.conn)
        product = dao.find_product(name)
        #print('result', result)
        if product is None:
            raise KeyError('Product {name} not found'.format(name))
                
        id = product.get_id()
        name = product.get_name()
        description = product.get_description()
        price = product.get_price()
        return {
            'id': id,
            'name': name,
            'description': description,
            'price': price
        }
        