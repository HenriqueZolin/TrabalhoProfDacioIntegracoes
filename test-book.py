import unittest
from book import Book  # Assuming the Book class is defined in book_module.py

class TestBook(unittest.TestCase):

    def test_criar_livro(self):
        livro = Book.adicionarLivro(
            "O Senhor dos Anéis",
            ["J.R.R. Tolkien"],
            "978-3-16-148410-0",
            1954,
            5,
            3
        )

        self.assertEqual(livro.titulo, "O Senhor dos Anéis")
        self.assertEqual(livro.autores, ["J.R.R. Tolkien"])
        self.assertEqual(livro.ISBN, "978-3-16-148410-0")
        self.assertEqual(livro.ano, 1954)
        self.assertEqual(livro.copiasTotal, 5)
        self.assertEqual(livro.copiasDisponiveis, 3)
        self.assertEqual(livro.status, "DISPONIVEL")
    

if __name__ == '__main__':
    unittest.main()