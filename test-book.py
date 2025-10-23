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

    def test_criar_livro_titulo_invalido(self):
        with self.assertRaises(ValueError) as context:
            Book.adicionarLivro(
                "",
                ["J.R.R. Tolkien"],
                "978-3-16-148410-0",
                1954,
                5,
                3
            )
        self.assertEqual(str(context.exception), "Título inválido")
    

    # --------------------------
    #  Rafael Gebara- função removerLivro
    # --------------------------
    def test_remover_livro(self):
        livro1 = Book.adicionarLivro("Livro 1", ["Autor 1"], "1234567890", 2000, 3, 3)
        livro2 = Book.adicionarLivro("Livro 2", ["Autor 2"], "0987654321", 2005, 2, 2)
        livros = [livro1, livro2]

        livros = Book.removerLivro(livros, "0987654321")

        self.assertEqual(len(livros), 1)
        self.assertEqual(livros[0].titulo, "Livro 1")

    def test_remover_livro_inexistente(self):
        livro = Book.adicionarLivro("Livro Único", ["Autor X"], "1234567890", 1999, 1, 1)
        livros = [livro]

        with self.assertRaises(ValueError) as context:
            Book.removerLivro(livros, "0000000000")
        self.assertEqual(str(context.exception), "Livro não encontrado para remoção")


if __name__ == '__main__':
    unittest.main()