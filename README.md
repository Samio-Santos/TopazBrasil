# TopazBrasil

## Descrição do Projeto

O objetivo deste projeto é obter dados do usuário através da API do GitHub, incluindo as seguintes informações:

- Nome
- Perfil
- Número de repositórios públicos
- Número de seguidores
- Número de usuários seguidos
- Lista de Repositórios

Além disso, o projeto permite criar um relatório do usuário em um arquivo "txt".

## Instruções de Uso

### Passo 1: Crie um Ambiente Virtual

No diretório principal do projeto, abra o terminal e execute o seguinte comando para criar um ambiente virtual:

python -m venv .venv


Em seguida, ative o ambiente virtual com base no seu sistema operacional:

**Windows:**

.venv\Scripts\activate.bat


**Linux/Mac:**

source .venv/bin/activate


### Passo 2: Instale as Dependências do Projeto

No diretório principal do projeto, onde se encontra o arquivo "requirements.txt", abra o terminal e execute o seguinte comando para instalar as dependências:

pip install -r requirements.txt


### Passo 3: Execute os Arquivos Python

#### Executar o Arquivo "request.py"

No diretório principal do projeto, onde se encontra o arquivo "request.py", abra o terminal e execute o seguinte comando para fazer uma requisição na API do GitHub e retornar informações do usuário:

python request.py


*Observação*: Este arquivo faz uma requisição na API do GitHub e retorna informações do usuário.

#### Executar o Arquivo "tests.py"

No diretório principal do projeto, onde se encontra o arquivo "tests.py", abra o terminal e execute o seguinte comando para executar os testes de unidade:

python tests.py


*Observação*: Este arquivo executa os testes de unidade.

#### Executar o Arquivo "test_integration.py"

No diretório principal do projeto, onde se encontra o arquivo "test_integration.py", abra o terminal e execute o seguinte comando para executar os testes de integração:

python test_integration.py


*Observação*: Este arquivo executa os testes de integração.
