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
📁 Cliente_Servidor

├── 📄 cliente.py # Código do cliente

├── 📄 servidor.py # Código do servidor

├── 📄 banco.db # Banco de dados SQLite (criado automaticamente)

└── 📄 README.md # Documentação do projeto


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
2️⃣ Instalar dependências

pip install fastapi uvicorn requests

---
3️⃣ Iniciar o servidor

uvicorn servidor:app --reload

---
4️⃣ Executar o cliente
python cliente.py

---
💻 Exemplo de uso

===== BANCO ONLINE =====
1. Criar conta
2. Login
3. Sair
Escolha (1-3): 1
Digite seu CPF: 12345678900
Crie uma senha: 1234
✅ Conta criada com sucesso!

---

📖 Aprendizados
📌 Como criar e consumir APIs REST com FastAPI

📌 Como estruturar aplicações Cliente/Servidor em Python

📌 Persistência de dados com SQLite

---

👩‍💻 Autora
Projeto desenvolvido por Andrea Cruz 🚀
