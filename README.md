# crud-python
 crud com python/flask
# Aplicação Web Flask

Esta é uma aplicação web Flask que combina duas funcionalidades principais:

1. **Gestão de Cursos**:
   - Os usuários podem visualizar uma lista de cursos com seus nomes, descrições e horas de crédito (ch).
   - Os usuários podem adicionar novos cursos, atualizar os existentes e excluí-los.

2. **Informações sobre Filmes**:
   - Os usuários podem acessar informações sobre filmes de várias categorias, como filmes populares, filmes infantis, filmes de um ano específico (2010 neste caso), filmes de drama e filmes com Tom Cruise.
   - Os dados do filme são obtidos na API The Movie Database (TMDb).

## Funcionalidades

- Adicionar, atualizar e excluir cursos com seus nomes, descrições e horas de crédito.
- Recuperar e exibir dados de filmes da API The Movie Database (TMDb) com base em diferentes categorias.
- Interface de usuário simples para interagir com cursos e dados de filmes.

## Tecnologias Utilizadas

- **Flask**: Um microframework web para Python.
- **SQLAlchemy**: Um toolkit SQL e biblioteca de Mapeamento Objeto-Relacional (ORM) para gerenciar dados de cursos.
- **API The Movie Database (TMDb)**: Usada para obter dados de filmes.
- **HTML/CSS**: Para renderizar páginas da web.
- **JavaScript (se aplicável)**: Para qualquer interatividade no lado do cliente (não presente no código fornecido).

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seunome/seu-aplicativo-flask.git

1.Navegue até o diretório do projeto:
cd seu-aplicativo-flask

2.Instale as dependências do projeto:
pip install -r requirements.txt

3.Configure o banco de dados:
python
>>> from your_app import db
>>> db.create_all()
>>> exit()

4.Execute a aplicação:
python seu_app.py

Uso
Acesse a aplicação web visitando http://localhost:5000/ em seu navegador da web.
Explore e gerencie cursos e filmes usando as interfaces fornecidas.

