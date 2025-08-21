# 💳 Banco Online - Cliente/Servidor com Python e FastAPI  

Este é um projeto simples de **banco online** implementado em Python utilizando o modelo **Cliente/Servidor**.  
O objetivo é treinar conceitos de **APIs REST**, **FastAPI** e **consumo de serviços** com Python.  

---

## 🚀 Tecnologias utilizadas
- 🐍 **Python 3**
- ⚡ **FastAPI** (servidor)
- 🔥 **Uvicorn** (servidor ASGI)
- 🌐 **Requests** (cliente)
- 💾 **SQLite** (banco de dados)

---

## 📂 Estrutura do projeto

Cliente_Servidor/

├── app/

│ ├── banco.py # Conexão SQLite e criação de tabela

│ ├── modelos.py # Modelos Pydantic (Conta)

│ └── servidor.py # Rotas da API

├── cliente.py # Cliente terminal que consome a API

├── requirements.txt # Dependências

└── banco.db # Banco SQLite (criado automaticamente)


## 🔎 Observações
 
> - O arquivo `banco.db` é criado automaticamente quando a API sobe pela primeira vez.

> - Se você não tiver o `__init__.py`, ainda funciona — mas é bom tê-lo para indicar pacote.

> - O `cliente.py` usa `BASE_URL = "http://127.0.0.1:8000"`. Se você publicar a API, troque pela URL pública.


---

## ⚙️ Funcionalidades
- 🆕 Criar conta com CPF e senha  
- 🔑 Fazer login  
- 💰 Consultar saldo  
- 💵 Realizar depósitos  
- 💸 Realizar saques  

---

## ▶️ Como executar

### 1️⃣ Clonar o repositório

git clone https://github.com/SEU_USUARIO/banco-online-python.git

cd banco-online-python

---
2️⃣ Instalar dependências:

pip install -r requirements.txt

---

3️⃣ Rodar o servidor:

uvicorn app.servidor:app --reload

---

4️⃣ Rodar o cliente (em outro terminal):

python cliente.py

---

📖 Aprendizados

📌 Como criar e consumir APIs REST com FastAPI

📌 Como estruturar aplicações Cliente/Servidor em Python

📌 Persistência de dados com SQLite

---

👩‍💻 Autora
Projeto desenvolvido por Andrea Cruz 🚀
