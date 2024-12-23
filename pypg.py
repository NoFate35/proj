import psycopg2
from psycopg2.extras import execute_batch, execute_values, NamedTupleCursor, RealDictCursor, LoggingCursor

try:
    # пытаемся подключиться к базе данных
    conn = psycopg2.connect(dbname='ivan', user='u0_a440',  host='/data/data/com.termux/files/usr/tmp')
except:
    # в случае сбоя подключения будет выведено сообщение в STDOUT
    print('Can`t establish connection to database')


sql0 = """DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS comments;"""
sql = '''CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    author_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE comments (
    post_id INTEGER NOT NULL,
    author_id INTEGER NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
'''
with conn:
    with conn.cursor() as cursor0:
        cursor0.execute(sql0)
        
with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            
def 
        