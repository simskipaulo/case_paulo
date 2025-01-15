# Paulo Case

Aplicação Web com permissão de cadastro de um produto, editar estoque, colocar preço e excluir.

## Funcionalidades

- 📂 Gerenciamento de dados de um produtos
- 📊 Relatórios.
- 📬 Integração com APIs externas

## Tecnologias Utilizadas

Este projeto foi desenvolvido com as seguintes tecnologias:

- [Python](https://www.python.org/) 3.x
- [Django](https://www.djangoproject.com/) 4.2.18
- [SQLite](https://www.sqlite.org/) (banco de dados)
- [Visual Studio Code](https://code.visualstudio.com/) (IDE)

## Pré-requisitos

Certifique-se de ter os seguintes itens instalados em sua máquina:

- Python 3.x
- Pip (gerenciador de pacotes Python)
- Um ambiente virtual configurado (opcional, mas recomendado)

## Instalação e Configuração

Siga os passos abaixo para configurar o projeto localmente:

1. Clone o repositório:
   ```bash
   git clone https://github.com/simskipaulo/case_paulo.git cd paulo_case
   
2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv env
   source env/bin/activate # Linux/Mac
   env\Scripts\activate # Windows
   
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt

4. Execute as migrações do banco de dados:
   ```bash
   python manage.py migrate
5. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
6. Acesse o projeto no navegador em http://localhost:8000.

## Estrutura do Projeto
   ```bash
├── paulo_case/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── static/
│   ├── css/
│   └── js/
├── paulo_app
│   ├── templates/
│   ├── migrations/
│   └── [arquivos.py]
├── db.sqlite3
└── manage.py
