import pytest
from catalogo import Catalogo, Livro 

@pytest.fixture
def catalogo():
    """
    Cria uma nova instância do Catalogo para cada teste.
    """
    return Catalogo()

# --- Testes dos Passos Iniciais (RED/GREEN) ---

def test_listar_livros_catalogo_vazio(catalogo):
    """
    Teste 1: Verifica se a listagem de um catálogo vazio retorna uma lista vazia.
    """
    livros = catalogo.listar_livros()
    assert livros == []
    assert len(livros) == 0

def test_listar_livros_com_itens(catalogo):
    """
    Teste 2: Verifica se a listagem retorna os livros que foram adicionados.
    (Nota: ISBNs estão sem hífens para passar na validação de 13 caracteres).
    """
    # PREPARAR (Arrange)
    catalogo.adicionar_livro(
        titulo="O Senhor dos Anéis",
        autores=["J.R.R. Tolkien"],
        isbn="9780618640157",  # <-- Corrigido (13 caracteres)
        ano=1954,
        copiasTotal=10,
        copiasDisponiveis=10
    )
    catalogo.adicionar_livro(
        titulo="1984",
        autores=["George Orwell"],
        isbn="9780451524935", # <-- Corrigido (13 caracteres)
        ano=1949,
        copiasTotal=5,
        copiasDisponiveis=5
    )

    # ATUAR (Act)
    livros = catalogo.listar_livros()

    # VERIFICAR (Assert)
    assert len(livros) == 2
    assert livros[0].titulo == "O Senhor dos Anéis"
    assert livros[1].titulo == "1984"

# --- Testes para a etapa REFACTOR ---

def test_refactor_status_dinamico(catalogo):
    """
    Teste 3: Testa se o 'status' (Refatoração 1) é dinâmico 
    e muda quando as cópias disponíveis chegam a zero.
    """
    livro = catalogo.adicionar_livro(
        titulo="Duna", autores=["Frank Herbert"], ano=1965, copiasTotal=1, copiasDisponiveis=1
    )
    
    assert livro.status == "DISPONIVEL"
    
    livro.copiasDisponiveis = 0 # Simula um empréstimo
    
    assert livro.status == "INDISPONIVEL"

def test_refactor_valida_titulo_vazio(catalogo):
    """
    Teste 4: Testa a validação de título (Refatoração 2).
    Não deve permitir adicionar livro com título vazio.
    """
    with pytest.raises(ValueError, match="Título deve ter entre 1 e 200 caracteres"):
        catalogo.adicionar_livro(
            titulo="", # Inválido
            autores=["Autor"], 
            ano=2020, 
            copiasTotal=1, 
            copiasDisponiveis=1
        )

def test_refactor_valida_isbn_unico(catalogo):
    """
    Teste 5: Testa a validação de ISBN único (Refatoração 2).
    Não deve permitir adicionar dois livros com o mesmo ISBN.
    """
    # Adiciona o primeiro livro
    catalogo.adicionar_livro(
        titulo="Livro A", 
        autores=["Autor A"], 
        ano=2020, 
        copiasTotal=1, 
        copiasDisponiveis=1, 
        isbn="1234567890" # ISBN válido de 10 dígitos
    )
    
    # Tenta adicionar o segundo livro com o MESMO ISBN
    with pytest.raises(ValueError, match="ISBN 1234567890 já existe"):
        catalogo.adicionar_livro(
            titulo="Livro B", 
            autores=["Autor B"], 
            ano=2021, 
            copiasTotal=1, 
            copiasDisponiveis=1, 
            isbn="1234567890" # ISBN Duplicado
        )