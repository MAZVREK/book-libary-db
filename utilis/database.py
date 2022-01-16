from .database_connection import DatabaseConnection


def create_book_table():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS books(id integer PRIMARY KEY AUTOINCREMENT, name text, author text, status integer)')



def add_book(name, author):
        with DatabaseConnection('data.db') as connection:
            cursor = connection.cursor()

            cursor.execute('INSERT INTO books(rowid, name, author, status) VALUES(NULL, ?, ?, 0)', (name, author))


def get_all_books():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM books')
        books = [{'id': row[0], 'name': row[1], 'author': row[2], 'status': row[3]} for row in cursor.fetchall()]
    return books


def mark_book_as_read(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE books SET status=1 WHERE name=?', (name,))



def delete_book(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM books WHERE name=?', (name,))
