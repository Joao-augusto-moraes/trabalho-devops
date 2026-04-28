import pytest
import crud

@pytest.fixture(autouse=True)
def clean_usuarios():
    # Limpa a lista de usuários antes de cada teste
    crud.usuarios.clear()

def test_criar_usuario():
    crud.criar_usuario(1, "Alice", 25)
    assert len(crud.usuarios) == 1
    assert crud.usuarios[0] == {"id": 1, "nome": "Alice", "idade": 25}

def test_listar_usuarios():
    crud.criar_usuario(1, "Alice", 25)
    crud.criar_usuario(2, "Bob", 30)
    usuarios = crud.listar_usuarios()
    assert len(usuarios) == 2
    assert usuarios[0]["nome"] == "Alice"
    assert usuarios[1]["nome"] == "Bob"

def test_buscar_usuario():
    crud.criar_usuario(1, "Alice", 25)
    usuario = crud.buscar_usuario(1)
    assert usuario is not None
    assert usuario["nome"] == "Alice"

    usuario_inexistente = crud.buscar_usuario(99)
    assert usuario_inexistente is None

def test_atualizar_usuario():
    crud.criar_usuario(1, "Alice", 25)
    
    # Atualiza apenas idade
    sucesso = crud.atualizar_usuario(1, nova_idade=26)
    assert sucesso is True
    usuario = crud.buscar_usuario(1)
    assert usuario["idade"] == 26
    assert usuario["nome"] == "Alice"
    
    # Atualiza nome
    crud.atualizar_usuario(1, novo_nome="Alice Silva")
    usuario = crud.buscar_usuario(1)
    assert usuario["nome"] == "Alice Silva"

def test_deletar_usuario():
    crud.criar_usuario(1, "Alice", 25)
    crud.criar_usuario(2, "Bob", 30)
    
    crud.deletar_usuario(1)
    assert len(crud.usuarios) == 1
    assert crud.buscar_usuario(1) is None
    assert crud.buscar_usuario(2) is not None