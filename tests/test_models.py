import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):

    def test_author_creation(self):
        author = Author(1, "John Doe")
        self.assertEqual(author.name, "John Doe")

    def test_article_creation(self):
       
        author = Author(1, "John Doe")
        magazine = Magazine(1, "Tech Weekly", "Technology")
     
        article = Article(author, magazine, "Test Article Title")

        self.assertEqual(article.title, "Test Article Title")
        self.assertEqual(article.author.id, 1)
        self.assertEqual(article.magazine.id, 1)

    def test_magazine_creation(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.category, "Technology")

if __name__ == "__main__":
    unittest.main()

