# models/author.py

from database.connection import get_db_connection

class Author:
    def __init__(self, id, name):
        self._id = id
        self.name = name

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = value

    def articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE author_id=?", (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return articles

    def magazines(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT magazines.* FROM magazines JOIN articles ON magazines.id = articles.magazine_id WHERE articles.author_id=?", (self.id,))
        magazines = cursor.fetchall()
        conn.close()
        return magazines

