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
        if(titulo.len() == 0 or titulo.len > 200):
            raise ValueError("Título inválido") 
        
        else:
            for autor in autores:
                if(autor.len() == 0 or autor.len() > 100):
                    raise ValueError("Autor inválido")
            
            if(len(isbn) != 10 or len(isbn) != 13):
                raise ValueError("ISBN inválido")
        
            elif(not isinstance(ano, int)):
                raise ValueError("Ano inválido")
        
            elif(copiasTotal < 0):
                raise ValueError("Número total de cópias inválido")
            
            elif(copiasDisponiveis < 0 or copiasDisponiveis > copiasTotal):
                raise ValueError("Número de cópias disponíveis inválido")

        return Book(titulo, autores, isbn, ano, copiasTotal, copiasDisponiveis)
    