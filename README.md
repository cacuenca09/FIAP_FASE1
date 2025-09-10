# Flask Recipes API

API construída em **Flask** para gerenciar receitas, com autenticação **JWT** e documentação interativa via **Swagger**.

---

## 🛠 Tecnologias

- Python 3.13  
- Flask  
- Flask SQLAlchemy  
- Flask-JWT-Extended  
- Flasgger (Swagger UI)  
- SQLite (local) / configurável via `config.py`  

---

## ⚡ Funcionalidades

- Registro e login de usuários com JWT  
- Rotas protegidas que exigem token  
- CRUD de receitas:
  - Criar receita (`POST /recipes`)  
  - Listar receitas (`GET /recipes`)  
  - Atualizar receita (`PUT /recipes/<id>`)  
- Filtros opcionais por ingrediente e tempo de preparo  
- Documentação interativa via Swagger (`/apidocs/`)  

---

## 🚀 Instalação

1. Clone o projeto:

```bash
git clone https://github.com/cacuenca09/FIAP_FASE1.git
cd FIAP_FASE1


