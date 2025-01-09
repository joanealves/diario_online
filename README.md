Diário Online
Este é um projeto de estudo desenvolvido com Python, utilizando o framework Django no back-end e HTML, CSS e JavaScript no front-end. O objetivo deste projeto foi criar um sistema de diário online simples, permitindo aos usuários registrar suas atividades e pensamentos de maneira intuitiva e prática.
![Screenshot_17](https://github.com/user-attachments/assets/88ed9eac-428a-4b71-bc81-994a0e7896f1)

Tecnologias Utilizadas
Back-end: Python, Django
Front-end: HTML, CSS, JavaScript
Banco de Dados: SQLite (padrão do Django)
Funcionalidades
Registro de entradas diárias com título, conteúdo e data.
Listagem de entradas anteriores.
Edição e exclusão de entradas.
Interface simples e responsiva.
Como Rodar o Projeto
Clone o repositório:

bash
Copiar código
git clone <URL_DO_REPOSITORIO>
Navegue até a pasta do projeto:

bash
Copiar código
cd <PASTA_DO_PROJETO>
Crie um ambiente virtual e ative-o:

bash
Copiar código
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Rode as migrações do banco de dados:

bash
Copiar código
python manage.py migrate
Inicie o servidor de desenvolvimento:

bash
Copiar código
python manage.py runserver
Acesse o projeto em: http://127.0.0.1:8000/
![Screenshot_18](https://github.com/user-attachments/assets/c4388509-3658-42e8-9611-14bea6b2182c)


OBS: Faltam algumas melhorias, como mensagens de erros, exclusão de post.. etc.
