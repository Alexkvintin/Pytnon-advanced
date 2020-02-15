import sqlite3


class ContextManager:

    def __init__(self, db):
        self._db = db

    def __enter__(self):
        self._conn = sqlite3.connect(self._db)
        self._cursor = self._conn.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._conn.commit()
        self._conn.close()
