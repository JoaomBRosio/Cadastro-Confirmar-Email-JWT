# Cadastro Confirmar Email JWT

Este projeto é um exemplo de como implementar um sistema de cadastro de usuários com confirmação de email utilizando JSON Web Tokens (JWT) em Python.

## Funcionalidades

- Cadastro de novos usuários
- Envio de email de confirmação
- Confirmação de email através de link com JWT
- Login de usuários

## Tecnologias Utilizadas

- Python
- Flask
- Flask-Mail
- PyJWT

## Instalação

1. Clone o repositório:
    ```bash
    https://github.com/JoaomBRosio/Cadastro-Confirmar-Email-JWT.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd cadastro_confirmarEmail_jwt
    ```
3. Crie um ambiente virtual:
    ```bash
    python -m venv venv
    ```
4. Ative o ambiente virtual:
    - No Windows:
        ```bash
        venv\Scripts\activate
        ```
    - No Linux/Mac:
        ```bash
        source venv/bin/activate
        ```
5. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Configuração

1. Renomeie o arquivo `.env.example` para `.env` e configure as variáveis de ambiente necessárias.

## Uso

1. Inicie o servidor:
    ```bash
    flask run
    ```
2. Use o Postman ou outra ferramenta para testar as rotas:

### Registro de Usuário
**URL:** `POST http://localhost:5000/register`

**JSON:**
```json
{
    "email": "usuario@example.com",
    "password": "senha123"
}
```

Verifique a caixa de entrada de seu email e confirme o mesmo.

### Login de Usuário
**URL:** `POST http://localhost:5000/login`

**JSON:**
```json
{
    "email": "usuario@example.com",
    "password": "senha123"
}
```

### Obter Todos os Usuários
**URL:** `GET http://localhost:5000/users`

### Deletar Todos os Usuários
**URL:** `DELETE http://localhost:5000/users`

## Estrutura do Projeto

- `app.py`: Arquivo principal da aplicação Flask.
- `models.py`: Definição do modelo de dados.
- `routes.py`: Definição das rotas da aplicação.
- `config.py`: Configurações da aplicação.
- `requirements.txt`: Dependências do projeto.