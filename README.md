# Projeto Simples - CRUD em Python

Este é um projeto básico para demonstrar um CRUD (Create, Read, Update e Delete) rápido feito inteiramente em Python, operando em memória (uma lista, sem a necessidade de um sistema de banco de dados externo) e que inclui também suporte à containerização (Docker) e Automação (CI/CD via GitHub Actions).

## 🗂 Estrutura do Projeto

* `crud.py`: Script principal que contém a lógica do CRUD em listas.
* `Dockerfile`: Configurações de passo a passo para empacotar e rodar a nossa aplicação dentro de um Container Docker.
* `requeriments.txt`: Arquivo com a listagem de dependências que a aplicação necessita para funcionar.
* `.github/workflows/ci-cd.yml`: Arquivo de Pipeline do GitHub Actions, acoplado para testar automaticamente e simular um Deploy a cada alteração aprovada para a branch `main`.

## 🚀 Como Executar Localmente

### Pelo Terminal do seu Computador (Tradicional)
1. Certifique-se de que o **Python (3.x)** se encontra instalado em sua máquina.
2. Pelo seu terminal, vá para a pasta raiz e rode o comando:
   ```bash
   python crud.py
   ```
   > Ou digite `python3 crud.py` (dependendo do seu Sistema Operacional)

### Através do Docker (Isolado)
1. Com o software Docker aberto rodando em sua máquina, crie a imagem rodando (não esqueça o ponto no final):
   ```bash
   docker build -t meu-crud-python .
   ```
2. Após carregar os dados e construir a imagem, crie e rode o container instantaneamente fazendo o seguinte:
   ```bash
   docker run --rm meu-crud-python
   ```

## ⚙️ Ação CI/CD (Pipeline)

Este repositório faz parte dos testes que usa o **GitHub Actions**. Com isto integrado, assim que existir um envio de código (`push` ou `pull_request`) na branch `main`:
1. Será configurado um ambiente livre de vícios com Ubuntu e Python 3.9.
2. Ação fará o pip install em cima do `requeriments.txt`.
3. Executa a prova para ver se houve alguma avaria no nosso `crud.py` criado.
4. Passando na prova, libera aviso para dar vazão à simulação de Deploy.

---
*Criado e desenvolvido como experimento didático e rápido!*
