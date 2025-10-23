# catalogo.py (VERSÃO REFATORADA)
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

    # --- REFATORAÇÃO 1: Status dinâmico ---
    # (O status agora é calculado, não armazenado)
    @property
    def status(self) -> Literal["DISPONIVEL", "INDISPONIVEL"]:
        return "DISPONIVEL" if self.copiasDisponiveis > 0 else "INDISPONIVEL"


class Catalogo:
    def __init__(self):
        self._livros: List[Livro] = []
        self._next_book_id: int = 1

    def _validar_isbn_unico(self, isbn: Optional[str]):
        """Método auxiliar para checar unicidade do ISBN"""
        if isbn is None: return True
        for livro in self._livros:
            if livro.isbn == isbn:
                raise ValueError(f"ISBN {isbn} já existe no catálogo.")
        return True

    def adicionar_livro(self, titulo: str, autores: List[str], ano: int, copiasTotal: int, copiasDisponiveis: int, isbn: Optional[str] = None, edicao: Optional[str] = None):

        # --- REFATORAÇÃO 2: Validações de dados (excelência) ---
        if not (1 <= len(titulo) <= 200):
            raise ValueError("Título deve ter entre 1 e 200 caracteres")
        if not autores or any(not (1 <= len(autor) <= 100) for autor in autores):
            raise ValueError("Autores devem ser listados e ter entre 1 e 100 caracteres")
        if isbn:
            if len(isbn) not in [10, 13]:
                raise ValueError("ISBN deve ter 10 ou 13 caracteres")
            self._validar_isbn_unico(isbn)
        if copiasTotal < 0 or copiasDisponiveis < 0 or copiasDisponiveis > copiasTotal:
            raise ValueError("Número de cópias inválido")
        # --- Fim da Refatoração 2 ---

        # (Note que 'status' não é mais passado no construtor do Livro)
        novo_livro = Livro(
            bookId=self._next_book_id,
            titulo=titulo,
            autores=autores,
            ano=ano,
            copiasTotal=copiasTotal,
            copiasDisponiveis=copiasDisponiveis,
            isbn=isbn,
            edicao=edicao
        )

        self._livros.append(novo_livro)
        self._next_book_id += 1
        return novo_livro

    def listar_livros(self) -> List[Livro]:
        return self._livros