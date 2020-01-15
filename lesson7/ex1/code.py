import sqlite3


class Con:

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.conn = sqlite3.connect(self.name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Закрываем подключение.
        """
        self.conn.close()


while True:
    f = input('для запуска нажмите 1')
    if f == '1':
            with Con('new.db') as conn:
                cursor = conn.cursor()
                try:
                    cursor.execute('INSERT INTO table_name (name, make, model, year) VALUES (2, 3, 4, 5000)')
                    conn.commit()
                    cursor.execute('SELECT * FROM table_name')
                    print(cursor.fetchall())
                except:
                    cursor.execute('CREATE TABLE table_name( id INTEGER, name TEXT, make TEXT, model TEXT, '
                                   'year INTEGER, '
                                   'PRIMARY KEY(id))')
                    conn.commit()
    else:
        break

