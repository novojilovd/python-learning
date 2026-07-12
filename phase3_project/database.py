import sqlite3
from sqlite3 import Cursor

def db_create(db_cursor: Cursor):
    db_cursor.execute('''CREATE TABLE IF NOT EXISTS author(
                        author_id INTEGER PRIMARY KEY,
                        name text NOT NULL
                        )''')
    db_cursor.execute('''CREATE TABLE IF NOT EXISTS books(
                        book_id INTEGER PRIMARY KEY,
                        author_id INTEGER NOT NULL,
                        book_type int NOT NULL,
                        FOREIGN KEY (author_id) REFERENCES author(author_id) ON DELETE CASCADE ON UPDATE CASCADE
                        )''')
    db_cursor.execute('''CREATE TABLE IF NOT EXISTS physical_books(
                        book_id INTEGER NOT NULL,
                        name text NOT NULL,
                        pages int NOT NULL,
                        ISBN text NOT NULL,
                        genre text NOT NULL,
                        publisher text NOT NULL,
                        weight real NOT NULL,
                        cover text NOT NULL,
                         FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE ON UPDATE CASCADE
                        )''')
    db_cursor.execute('''CREATE TABLE IF NOT EXISTS digital_books(
                        book_id INTEGER NOT NULL,
                        name text NOT NULL,
                        pages int NOT NULL,
                        ISBN text NOT NULL,
                        genre text NOT NULL,
                        publisher text NOT NULL,
                        size real NOT NULL,
                        file_path text NOT NULL,
                         FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE ON UPDATE CASCADE
                        )''')

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
    db_cursor.execute('''INSERT INTO books(book_type) VALUES (?)''', (entity_type,))
    book_id = db_cursor.lastrowid
    match entity_type:
        case 1:
            db_cursor.execute('''INSERT INTO physical_books(book_id, 
                                                                name, 
                                                                pages, 
                                                                ISBN, 
                                                                genre, 
                                                                publisher, 
                                                                weigth, 
                                                                cover) 
                                 VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                              (book_id,
                                         kwargs['name'],
                                         kwargs['pages'],
                                         kwargs['ISBN'],
                                         kwargs['genre'],
                                         kwargs['publisher'],
                                         kwargs['weight'],
                                         kwargs['cover']))
        case 2:
            db_cursor.execute('''INSERT INTO digital_books(book_id, 
                                                                name, 
                                                                pages, 
                                                                ISBN, 
                                                                genre, 
                                                                publisher, 
                                                                size, 
                                                                file_path) 
                                 VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                              (book_id,
                                         kwargs['name'],
                                         kwargs['pages'],
                                         kwargs['ISBN'],
                                         kwargs['genre'],
                                         kwargs['publisher'],
                                         kwargs['size'],
                                         kwargs['file_path']))
        case _:
            print("Что-то пошло не так")
if __name__ == '__main__':
    db_cursor = db_init()