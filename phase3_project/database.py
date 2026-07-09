import sqlite3
from sqlite3 import Cursor

def db_create(db_cursor: Cursor):
    db_cursor.execute('''CREATE TABLE IF NOT EXISTS books(
                        book_id INTEGER PRIMARY KEY,
                        book_type int NOT NULL
                        )''')
    db_cursor.execute('''CREATE TABLE IF NOT EXISTS physical_books(
                        book_id INTEGER NOT NULL,
                        name text NOT NULL,
                        pages int NOT NULL,
                        author text NOT NULL,
                        ISBN text NOT NULL,
                        genre text NOT NULL,
                        publisher text NOT NULL,
                        weight real NOT NULL,
                        cover text NOT NULL,
                         FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE ON UPDATE CASCADE)''')
    db_cursor.execute('''CREATE TABLE IF NOT EXISTS digital_books(
                        book_id INTEGER NOT NULL,
                        name text NOT NULL,
                        pages int NOT NULL,
                        author text NOT NULL,
                        ISBN text NOT NULL,
                        genre text NOT NULL,
                        publisher text NOT NULL,
                        size real NOT NULL,
                        file_path text NOT NULL,
                         FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE ON UPDATE CASCADE)''')
def db_init() -> Cursor:
    conn = sqlite3.connect('database.db')
    db_cursor = conn.cursor()
    try:
        db_cursor.execute('''select * from books''').fetchall()
    except sqlite3.OperationalError:
        print('База данных не обнаружена, пересоздание')
        db_create(db_cursor)
        print('База данных создана')
    return db_cursor

def db_insert(entity_type: int, db_cursor: Cursor, **kwargs) -> None:
    match entity_type:
        case 1:
            db_cursor.execute('''INSERT INTO''')
        case 2:
            db_cursor.execute('''INSERT INTO''')

if __name__ == '__main__':
    db_cursor = db_init()
    db_create(db_cursor)