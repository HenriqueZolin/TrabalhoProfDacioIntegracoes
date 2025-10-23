import itertools

class Book:
    id_iter = itertools.count()

    def __init__(self, titulo, autores, isbn, ano, copiasTotal, copiasDisponiveis):
        self.bookId = next(Book.id_iter)
        self.titulo = titulo
        self.autores = autores
        self.ISBN = isbn
        self.edicao = None
        self.ano = ano
        self.copiasTotal = copiasTotal
        self.copiasDisponiveis = copiasDisponiveis
        self.status = "DISPONIVEL" if copiasDisponiveis > 0 else "INDISPONIVEL"

    @staticmethod
    def adicionarLivro(titulo, autores, isbn, ano, copiasTotal, copiasDisponiveis):
        if len(titulo) == 0 or len(titulo) > 200:
            raise ValueError("Título inválido")

        for autor in autores:
            if len(autor) == 0 or len(autor) > 100:
                raise ValueError("Autor inválido")

        isbn_limpo = isbn.replace("-", "")
        if len(isbn_limpo) not in (10, 13):
            raise ValueError("ISBN inválido")

        if not isinstance(ano, int):
            raise ValueError("Ano inválido")

        if copiasTotal < 0:
            raise ValueError("Número total de cópias inválido")

        if copiasDisponiveis < 0 or copiasDisponiveis > copiasTotal:
            raise ValueError("Número de cópias disponíveis inválido")

        return Book(titulo, autores, isbn, ano, copiasTotal, copiasDisponiveis)

    @staticmethod
    def removerLivro(listaLivros, isbn):
        if not isinstance(listaLivros, list):
            raise ValueError("A lista de livros deve ser uma lista válida")

        if not any(livro.ISBN == isbn for livro in listaLivros):
            raise ValueError("Livro não encontrado para remoção")

        nova_lista = [livro for livro in listaLivros if livro.ISBN != isbn]
        return nova_lista

    @staticmethod
    def listarLivros(listaLivros):
        if not isinstance(listaLivros, list):
            raise ValueError("A lista de livros deve ser uma lista válida")
        
        return [
            (
                f"ID: {livro.bookId}, Título: {livro.titulo}, "
                f"Autores: {', '.join(livro.autores)}, ISBN: {livro.ISBN}, "
                f"Status: {livro.status}"
            )
            for livro in listaLivros
        ]

    # ------------------------------------------------
    # Novas funcionalidades (TDD Green)
    # ------------------------------------------------
    def emprestarLivro(self):
        """Reduz 1 cópia disponível e atualiza o status."""
        if self.copiasDisponiveis <= 0:
            raise ValueError("Não há cópias disponíveis para empréstimo.")
        
        self.copiasDisponiveis -= 1
        if self.copiasDisponiveis == 0:
            self.status = "INDISPONIVEL"

    def devolverLivro(self):
        """Aumenta 1 cópia disponível e atualiza o status."""
        if self.copiasDisponiveis >= self.copiasTotal:
            raise ValueError("Todas as cópias já estão disponíveis.")
        
        self.copiasDisponiveis += 1
        if self.copiasDisponiveis > 0:
            self.status = "DISPONIVEL"
