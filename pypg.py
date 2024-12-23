import psycopg2
from psycopg2.extras import execute_batch, execute_values, NamedTupleCursor, RealDictCursor, LoggingCursor, DictCursor

try:
    # пытаемся подключиться к базе данных
    conn = psycopg2.connect(dbname='hexlet', user='ivan',  host='/var/run/postgresql')
    #conn = psycopg2.connect(dbname='ivan', user='u0_a440',  host='/data/data/com.termux/files/usr/tmp')
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
post = {'title': 'My Super Post', 'content': 'text', 'author_id': 42}
post1 = {'title': 'FFFFFFUUU', 'content': "uuuuuuuu", 'author_id': 8}
def create_post(conn, post):
     with conn:
          with conn.cursor() as cursor:
                  sql = """INSERT INTO posts (title, content, author_id)
                           VALUES (%(title)s, %(content)s, %(author_id)s);"""
                  cursor.execute(sql,post)
                  sql1 = """SELECT id FROM posts WHERE title =  %(title)s AND content = %(content)s AND author_id = %(author_id)s"""
                  cursor.execute(sql1, post)
                  rez = cursor.fetchone()
     return rez[0]
            
post_id = create_post(conn, post)
create_post(conn, post1)

comment_1 = {'post_id': post_id, 'author_id': 42, 'content': 'wow such post'}
comment_2 = {'post_id': post_id, 'author_id': 24, 'content': 'totally disagree btw i use arch'}

def add_comment(conn, comment):
     sql = """INSERT INTO comments (post_id, author_id, content)
                VALUES (%(post_id)s, %(author_id)s, %(content)s)"""
     with conn:
          with conn.cursor() as cursor:
               cursor.execute(sql, comment)

add_comment(conn, comment_1)
add_comment(conn, comment_2)

#SELECT p.id, p.title, p.content, p.author_id, p.created_at, c.author_id, c.content, c.created_at FROM posts p LEFT JOIN comments c ON p.id = c.post_id;

def get_latest_posts(conn, number):
     sql = """SELECT id, title, content, author_id, created_at FROM posts ORDER BY created_at DESC LIMIT %(number)s;"""
     sql1 = """SELECT post_id AS id, author_id, content, created_at FROM comments WHERE post_id = %(post_id)s"""
     with conn:
          with conn.cursor(cursor_factory=RealDictCursor) as cursor:
               cursor.execute(sql, {'number': number})
               posts = cursor.fetchall()
     conn.commit()
     conn.close()
     with conn:
          with conn.cursor(cursor_factory=RealDictCursor) as cursor:
               for post in posts:
                    post_id = post['id']
                    cursor.execute(sql1, {'post_id': post_id})
                    comments = cursor.fetchall()
                    if comments:
                         post['comments'] = comments
     return posts



get_latest_posts(conn, 3)