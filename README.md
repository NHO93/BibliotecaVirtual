# 📚 Biblioteca Virtual

Uma aplicação web desenvolvida em **Django** para gerenciar coleções de livros. Os usuários podem criar, visualizar, editar e excluir suas próprias coleções, além de listar livros disponíveis.

---

## 🚀 Funcionalidades

- Cadastro e autenticação de usuários.
- Criação, edição e exclusão de coleções de livros.
- Listagem de livros e coleções.
- Permissões de acesso:
  - Apenas o proprietário pode editar ou excluir sua coleção.
  - Usuários autenticados podem visualizar coleções públicas.
- Integração com o painel administrativo do Django.
- API REST para operações CRUD, documentada com **drf-spectacular**.

---

## 🛠️ Tecnologias Utilizadas

- **Backend**:
  - Django
  - Django REST Framework
  - Django REST Framework SimpleJWT (autenticação por tokens)
  - drf-spectacular (documentação da API)
  - SQLite (banco de dados)
- **Outros**:
  - Python 3.10+
  - Django CORS Headers

---

## ⚙️ Instalação e Configuração

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/biblioteca-virtual.git
cd biblioteca-virtual
```

### 2. Crie um ambiente virtual
```bash
python -m venv venv
```

Ative o ambiente:
- **Windows**:
  ```bash
  .\venv\Scripts\activate
  ```
- **Linux/macOS**:
  ```bash
  source venv/bin/activate
  ```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Aplique as migrações
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crie um superusuário
```bash
python manage.py createsuperuser
```

### 6. Inicie o servidor de desenvolvimento
```bash
python manage.py runserver
```

Acesse a aplicação no navegador em [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## 🔗 Endpoints da API

Abaixo estão alguns dos principais endpoints disponíveis:

### **Autenticação**
- `POST /api/token/`: Gera o token de autenticação.
- `POST /api/token/refresh/`: Atualiza o token.

### **Coleções**
- `GET /api/colecoes/`: Lista todas as coleções.
- `POST /api/colecoes/`: Cria uma nova coleção.
- `GET /api/colecoes/<id>/`: Detalha uma coleção específica.
- `PUT /api/colecoes/<id>/`: Atualiza uma coleção específica.
- `DELETE /api/colecoes/<id>/`: Remove uma coleção específica.

### **Documentação**
Acesse a documentação da API em [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/).

---

## 📄 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---
