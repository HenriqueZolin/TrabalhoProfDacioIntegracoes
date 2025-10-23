# catalogo.py
from dataclasses import dataclass, field
from typing import List, Optional, Literal

@dataclass
class Livro:
    bookId: int
    titulo: str
    autores: List[str]
    ano: int
    copiasTotal: int
    copiasDisponiveis: int
    isbn: Optional[str] = None 
    edicao: Optional[str] = None 
    status: Literal["DISPONIVEL", "INDISPONIVEL"] = "DISPONIVEL" # Versão simples


class Catalogo:
    def __init__(self):
        self._livros: List[Livro] = []
        self._next_book_id: int = 1

    def adicionar_livro(self, titulo: str, autores: List[str], ano: int, copiasTotal: int, copiasDisponiveis: int, isbn: Optional[str] = None, edicao: Optional[str] = None):
        """
        Versão SIMPLES para fazer o teste passar.
        """
        status_livro = "DISPONIVEL" if copiasDisponiveis > 0 else "INDISPONIVEL"

        novo_livro = Livro(
            bookId=self._next_book_id,
            titulo=titulo,
            autores=autores,
            ano=ano,
            copiasTotal=copiasTotal,
            copiasDisponiveis=copiasDisponiveis,
            isbn=isbn,
            edicao=edicao,
            status=status_livro
        )

        self._livros.append(novo_livro)
        self._next_book_id += 1
        return novo_livro

    def listar_livros(self) -> List[Livro]:
        """
        Funcionalidade 4 - Lstar (RAFAEL)
        """
        return self._livros