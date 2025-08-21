 
from fastapi import FastAPI, HTTPException
from app.modelos import Conta
from app.banco import conectar, criar_tabela

# Inicializa FastAPI
app = FastAPI(title="Banco Online", description="Servidor do Banco Online")

# Cria tabela no banco
criar_tabela()

# Rota para criar conta
@app.post("/criar_conta")
def criar_conta(conta: Conta):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contas WHERE cpf=?", (conta.cpf,))
    if cursor.fetchone():
        conn.close()
        raise HTTPException(status_code=400, detail="Conta já existe")
    cursor.execute("INSERT INTO contas (cpf, senha, saldo) VALUES (?, ?, ?)",
                   (conta.cpf, conta.senha, conta.saldo))
    conn.commit()
    conn.close()
    return {"mensagem": "Conta criada com sucesso!"}

# Rota para login
@app.post("/login")
def login(cpf: str, senha: str):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contas WHERE cpf=? AND senha=?", (cpf, senha))
    if not cursor.fetchone():
        conn.close()
        raise HTTPException(status_code=401, detail="CPF ou senha incorretos")
    conn.close()
    return {"mensagem": "Login realizado com sucesso!"}

# Rota para consultar saldo
@app.get("/saldo/{cpf}")
def saldo(cpf: str, senha: str):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT saldo FROM contas WHERE cpf=? AND senha=?", (cpf, senha))
    resultado = cursor.fetchone()
    conn.close()
    if not resultado:
        raise HTTPException(status_code=401, detail="CPF ou senha incorretos")
    return {"saldo": resultado[0]}

# Rota para depósito
@app.post("/deposito")
def deposito(cpf: str, senha: str, valor: float):
    if valor <= 0:
        raise HTTPException(status_code=400, detail="Valor inválido")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT saldo FROM contas WHERE cpf=? AND senha=?", (cpf, senha))
    resultado = cursor.fetchone()
    if not resultado:
        conn.close()
        raise HTTPException(status_code=401, detail="CPF ou senha incorretos")
    saldo_atual = resultado[0] + valor
    cursor.execute("UPDATE contas SET saldo=? WHERE cpf=?", (saldo_atual, cpf))
    conn.commit()
    conn.close()
    return {"mensagem": f"Depósito de R${valor:.2f} realizado!", "saldo": saldo_atual}

# Rota para saque
@app.post("/saque")
def saque(cpf: str, senha: str, valor: float):
    if valor <= 0:
        raise HTTPException(status_code=400, detail="Valor inválido")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT saldo FROM contas WHERE cpf=? AND senha=?", (cpf, senha))
    resultado = cursor.fetchone()
    if not resultado:
        conn.close()
        raise HTTPException(status_code=401, detail="CPF ou senha incorretos")
    if resultado[0] < valor:
        conn.close()
        raise HTTPException(status_code=400, detail="Saldo insuficiente")
    saldo_atual = resultado[0] - valor
    cursor.execute("UPDATE contas SET saldo=? WHERE cpf=?", (saldo_atual, cpf))
    conn.commit()
    conn.close()
    return {"mensagem": f"Saque de R${valor:.2f} realizado!", "saldo": saldo_atual}

# Rodar servidor local
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("servidor:app", host="0.0.0.0", port=8000, reload=True)
