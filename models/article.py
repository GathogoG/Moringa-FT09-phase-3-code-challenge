from database.connection import get_db_connection

class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
    
    def get_author_id(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM authors WHERE name=?", (self.author.name,))
        result = cursor.fetchone()
        conn.close()
        if result:
            return result["id"]
        else:
            raise ValueError(f"Author '{self.author.name}' not found in database.")

