import psycopg2
from productDAO import ProductDAO

try:
    # пытаемся подключиться к базе данных
    conn = psycopg2.connect(dbname='hexlet', user='ivan',  host='/var/run/postgresql')
    #conn = psycopg2.connect(dbname='ivan', user='u0_a440',  host='/data/data/com.termux/files/usr/tmp')
except:
    # в случае сбоя подключения будет выведено сообщение в STDOUT
    print('Can`t establish connection to database')
    
class Catalog (self, conn):
    def __init__(self, conn):
        self.conn = conn
    