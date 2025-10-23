import unittest
import itertools
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
#RAFAEL TUDELA
    def setUp(self):
       
        Book.id_iter = itertools.count()

    def test_listar_livros_lista_vazia(self):
        livros = []
        resultado = Book.listarLivros(livros)
        self.assertEqual(resultado, [])

    def test_listar_livros_com_um_livro(self):
        
        livro = Book.adicionarLivro("O Hobbit", ["J.R.R. Tolkien"], "1234567890", 1937, 2, 2)
        livros = [livro]
        resultado = Book.listarLivros(livros)
        
        expected_output = [
            "ID: 0, Título: O Hobbit, Autores: J.R.R. Tolkien, ISBN: 1234567890, Status: DISPONIVEL"
        ]
        self.assertEqual(resultado, expected_output)
        
    def test_listar_livros_multiplos(self):
       
        livro1 = Book.adicionarLivro("O Hobbit", ["J.R.R. Tolkien"], "1234567890", 1937, 2, 2)
        livro2 = Book.adicionarLivro(
            "O Nome do Vento", 
            ["Patrick Rothfuss"], 
            "9876543210", 
            2007, 
            1, 
            0 
        )
        livro3 = Book.adicionarLivro(
            "Good Omens", 
            ["Terry Pratchett", "Neil Gaiman"],
            "5555555555", 
            1990, 
            5, 
            5
        )
        livros = [livro1, livro2, livro3]
        resultado = Book.listarLivros(livros)

        expected_output = [
            "ID: 0, Título: O Hobbit, Autores: J.R.R. Tolkien, ISBN: 1234567890, Status: DISPONIVEL",
            "ID: 1, Título: O Nome do Vento, Autores: Patrick Rothfuss, ISBN: 9876543210, Status: INDISPONIVEL",
            "ID: 2, Título: Good Omens, Autores: Terry Pratchett, Neil Gaiman, ISBN: 5555555555, Status: DISPONIVEL"
        ]
        self.assertEqual(resultado, expected_output)

    def test_listar_livros_input_invalido(self):
        
        with self.assertRaises(ValueError) as context:
            Book.listarLivros("não sou uma lista")
        self.assertEqual(str(context.exception), "A lista de livros deve ser uma lista válida")

if __name__ == '__main__':
    unittest.main()