from blog_post import Post
import sqlite3


def get_db_connection():
    conn = sqlite3.connect('blogdatabase.db')
    conn.row_factory = sqlite3.Row
    return conn, conn.cursor()


def close_db_connection(conn):
    conn.close()


def init_db():
    conn, cursor = get_db_connection()

    cursor.execute('''CREATE TABLE IF NOT EXISTS posts
                       (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT,
                        content TEXT,
                        author TEXT,
                        published_date TEXT)''')

    conn.commit()
    close_db_connection(conn)


def add_post(title, content, author, published_date):
    conn, cursor = get_db_connection()

    cursor.execute('''INSERT INTO posts
                       (title, content, author, published_date)
                       VALUES (?, ?, ?, ?)''',
                   (title, content, author, published_date))

    conn.commit()
    close_db_connection(conn)


def get_posts():
    conn, cursor = get_db_connection()

    cursor.execute('SELECT * FROM posts')

    posts = []

    for row in cursor.fetchall():
        post = Post(row['id'], row['title'], row['content'],
                    row['author'], row['published_date'])
        posts.append(post)

    close_db_connection(conn)

    return posts
