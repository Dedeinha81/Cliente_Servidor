  
import sqlite3

# Função para conectar ao banco SQLite
def conectar():
    conexao = sqlite3.connect("banco.db")
    return conexao

# Função para criar tabela de contas, se não existir
def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contas (
            cpf TEXT PRIMARY KEY,
            senha TEXT NOT NULL,
            saldo REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()
