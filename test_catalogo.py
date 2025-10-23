# test_catalogo.py
import pytest
from catalogo import Catalogo, Livro # <-- Isso vai falhar (RED)

@pytest.fixture
def catalogo():
    return Catalogo()

def test_listar_livros_catalogo_vazio(catalogo):
    """
    Teste 1 (RED): Se o catálogo está vazio, listar_livros() deve retornar uma lista vazia.
    """
    livros = catalogo.listar_livros()
    assert livros == []
    assert len(livros) == 0

def test_listar_livros_com_itens(catalogo):
    """
    Teste 2 (RED): Se adicionarmos livros, listar_livros() deve retornar uma lista com eles.
    """
    catalogo.adicionar_livro(
        titulo="O Senhor dos Anéis",
        autores=["J.R.R. Tolkien"],
        isbn="978-0618640157",
        ano=1954,
        copiasTotal=10,
        copiasDisponiveis=10
    )
    catalogo.adicionar_livro(
        titulo="1984",
        autores=["George Orwell"],
        isbn="978-0451524935",
        ano=1949,
        copiasTotal=5,
        copiasDisponiveis=5
    )

    livros = catalogo.listar_livros()

    assert len(livros) == 2
    assert livros[0].titulo == "O Senhor dos Anéis"
    assert livros[1].titulo == "1984"