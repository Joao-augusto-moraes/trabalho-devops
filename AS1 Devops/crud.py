# crud.py

# Banco de dados em memória (uma simples lista)
usuarios = []

# C - Create (Criar)
def criar_usuario(id, nome, idade):
    usuario = {"id": id, "nome": nome, "idade": idade}
    usuarios.append(usuario)
    print(f"Usuário '{nome}' criado com sucesso!")

# R - Read (Ler)
def listar_usuarios():
    return usuarios

def buscar_usuario(id):
    for usuario in usuarios:
        if usuario["id"] == id:
            return usuario
    return None

# U - Update (Atualizar)
def atualizar_usuario(id, novo_nome=None, nova_idade=None):
    usuario = buscar_usuario(id)
    if usuario:
        if novo_nome:
            usuario["nome"] = novo_nome
        if nova_idade:
            usuario["idade"] = nova_idade
        print(f"Usuário ID {id} atualizado com sucesso!")
        return True
    print(f"Usuário ID {id} não encontrado.")
    return False

# D - Delete (Deletar)
def deletar_usuario(id):
    global usuarios
    # Mantém na lista apenas quem não tem o ID informado
    usuarios = [usuario for usuario in usuarios if usuario["id"] != id]
    print(f"Usuário ID {id} deletado com sucesso!")

# Testando nosso CRUD
if __name__ == "__main__":
    print("--- CRIANDO USUÁRIOS ---")
    criar_usuario(1, "João", 25)
    criar_usuario(2, "Maria", 30)
    
    print("\n--- LENDO USUÁRIOS ---")
    print(listar_usuarios())
    
    print("\n--- ATUALIZANDO USUÁRIO ---")
    atualizar_usuario(1, nova_idade=26)
    print("Como ficou o João:", buscar_usuario(1))
    
    print("\n--- DELETANDO USUÁRIO ---")
    deletar_usuario(2)
    
    print("\n--- LENDO USUÁRIOS NOVAMENTE ---")
    print(listar_usuarios())
