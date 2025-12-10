Projeto de Blog

Este é um sistema web desenvolvido com Django, HTML, JavaScript, Bootstrap e banco de dados PostgrSql, que permite que usuários criem post sobre diversos temas e que possam serem vistos por outros usuários. O sistema oferece autenticação de usuário, redefinição de senha e dados pessoais, criação de posts, atualização, exclusão e listagem em uma parte pessoal do usuário, ainda um área de filtragem por tag e área de listagem de posts de diversos usuários. Há pesquisa por titulo e conteúdo na barra de navegação.

---
## 🚀 TECNOLOGIAS UTILIZADAS
  -  Python 
  -  Django Framework
  -  Docker
  -  PostgreSQL
  -  HTML
  -  Bootstrap
  -  JavaScript

---


## 🎯 Funcionalidades
---
## 🔐 AUTENTICAÇÃO DE USUÁRIO

A ao usuário tentar usar qualquer funcionalidade será redirecionado para a àrea de autenticação (login/cadastro)
Serão requisitados as seguintes informações nas seguintes telas:
    
    Tela de cadastro:
        Nome de usuário
        E-mail
        senha
        confirmação de senha

    Tela de login:
        Nome de usuário
        Senha
---

---
## 🏠 TELAS APÓS AUTENTICAÇÃO

Após autenticação, o usuário tem acesso as seguintes funcionalidades:

    HOME 
        Apresenta todos os posts feitos por usuários.
    
    Post
        Local onde usuários criam seus post / listagem / atualização / exclusão

    Tags
        Local onde tem as tags de busca de posts

    Perfil
        Tela com botões de ações para editar dados / alterar senha / desativar conta

    Editar dados
        Tela apresenta formulário com dados referente ao cadastro e que podem ser atualizados

    Alterar senha
        Tela apresenta 3 campos a serem preenchidos: antiga senha / nova senha / confirmação de senha
    
    desativar conta 
        Desativa o acesso do usuário no mesmo momento.
---

---

## 🔒 PROTEÇÃO

    Cada post é vinculado ao usuário autenticado no momento da criação
    É utilizado um dispatch personalizado para verificar o usuário na atualização
    É utilizado um comparador do campo user no post para comparar com o usuário no momento da exclusão
    Uma mensagem é exibida quando um usuário que não tem permissão de acesso tenta acessar:
    'Você não tem permissão para acessar ou editar este post.'

---
## Como Executar o Projeto

### 1. Clone o repositório
```bash
https://github.com/ErickIgles/My_Blog.git
cd seu-repositorios
```


### 2. Crie e ative um ambiente virtual

```bash
# Para criar ambiente virtual
python -m venv venv

# Para ativar

# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Instale as dependências
```bah
pip install -r requirements.txt
```


### 4. Configure as variáveis de ambiente
Crie um arquivo .env na raiz do projeto com:

```bash
SECRET_KEY=sua_chave_secreta

POSTGRES_DB=blog_db
POSTGRES_USER=blog_user
POSTGRES_PASSWORD=blog_password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

### 5. Suba o PostgreSQL com Docker
Certifique-se de que seu arquivo docker-compose.yml está assim:
```bash
services:
  db:
    image: postgres:16
    container_name: postgres_django
    restart: always
    ports:
      - "5432:5432"
    environment:
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    env_file:
      - .env
    volumes:
      - ./data/postgresql_data:/var/lib/postgresql/data

execute: docker compose up -d
```

### 6. Aplique as migrações
```bash
python manage.py migrate
```

### 7. Crie um superusuário (opcional)
```bash
python manage.py createsuperuser
```

### 8. Execute o servidor
```bash
python manage.py runserver

Acesse o sistema em: http://127.0.0.1:8000/

Acesse o admin em: http://127.0.0.1:8000/admin/
```
