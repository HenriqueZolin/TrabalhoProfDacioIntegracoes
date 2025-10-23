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

    def adicionarLivro(titulo, autores, isbn, ano, copiasTotal, copiasDisponiveis):
        return Book(titulo, autores, isbn, ano, copiasTotal, copiasDisponiveis)
    