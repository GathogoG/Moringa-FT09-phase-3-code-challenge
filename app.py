from database.setup import create_tables
from database.connection import get_db_connection
from models.author import Author
from models.magazine import Magazine
from models.article import Article

def main():
    # Initialize the database and create tables
    create_tables()

    # Collect user input
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")

    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Create an author
        cursor.execute('INSERT INTO authors (name) VALUES (?)', (author_name,))
        author_id = cursor.lastrowid

        # Create a magazine
        cursor.execute('INSERT INTO magazines (name, category) VALUES (?,?)', (magazine_name, magazine_category))
        magazine_id = cursor.lastrowid

        # Create an article
        cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
                       (article_title, article_content, author_id, magazine_id))

        conn.commit()

        # Query the database to retrieve inserted records
        cursor.execute('SELECT * FROM magazines')
        magazines = cursor.fetchall()

        cursor.execute('SELECT * FROM authors')
        authors = cursor.fetchall()

        cursor.execute('SELECT * FROM articles')
        articles = cursor.fetchall()

        conn.close()

        # Display results
        print("\nMagazines:")
        for magazine in magazines:
            print(f"ID: {magazine['id']}, Name: {magazine['name']}, Category: {magazine['category']}")

        print("\nAuthors:")
        for author in authors:
            print(f"ID: {author['id']}, Name: {author['name']}")

        print("\nArticles:")
        for article in articles:
            print(f"ID: {article['id']}, Title: {article['title']}, Content: {article['content']}, Author ID: {article['author_id']}, Magazine ID: {article['magazine_id']}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        conn.rollback()

if __name__ == "__main__":
    main()

