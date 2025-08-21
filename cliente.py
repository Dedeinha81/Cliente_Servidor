
# Cliente para interagir com o servidor do Banco Online

import requests  # Biblioteca para fazer requisições HTTP

# URL do servidor FastAPI
BASE_URL = "http://127.0.0.1:8000"

# Função para criar uma conta
def criar_conta():
    cpf = input("Digite seu CPF: ")
    senha = input("Crie uma senha: ")
    
    try:
        # Faz requisição POST para criar conta
        response = requests.post(
            f"{BASE_URL}/criar_conta", 
            json={"cpf": cpf, "senha": senha, "saldo": 0.0}
        )
        # Verifica se a resposta foi sucesso
        if response.status_code == 200:
            print(response.json().get("mensagem"))
        else:
            print("Erro:", response.json().get("detail"))
    except requests.exceptions.RequestException as e:
        print("Erro na conexão:", e)

# Função para login
def login():
    cpf = input("Digite seu CPF: ")
    senha = input("Digite sua senha: ")
    
    try:
        response = requests.post(
            f"{BASE_URL}/login", 
            params={"cpf": cpf, "senha": senha}
        )
        if response.status_code == 200:
            print(response.json().get("mensagem"))
            return cpf, senha
        else:
            print("Erro:", response.json().get("detail"))
            return None, None
    except requests.exceptions.RequestException as e:
        print("Erro na conexão:", e)
        return None, None

# Função para consultar saldo
def consultar_saldo(cpf, senha):
    try:
        response = requests.get(
            f"{BASE_URL}/saldo/{cpf}", 
            params={"senha": senha}
        )
        if response.status_code == 200:
            print(f"Seu saldo é: R${response.json()['saldo']:.2f}")
        else:
            print("Erro:", response.json().get("detail"))
    except requests.exceptions.RequestException as e:
        print("Erro na conexão:", e)

# Função para depósito
def realizar_deposito(cpf, senha):
    try:
        valor = float(input("Digite o valor do depósito: "))
        response = requests.post(
            f"{BASE_URL}/deposito",
            params={"cpf": cpf, "senha": senha, "valor": valor}
        )
        if response.status_code == 200:
            print(response.json().get("mensagem"))
            print(f"Saldo atual: R${response.json()['saldo']:.2f}")
        else:
            print("Erro:", response.json().get("detail"))
    except ValueError:
        print("Digite um valor válido!")
    except requests.exceptions.RequestException as e:
        print("Erro na conexão:", e)

# Função para saque
def realizar_saque(cpf, senha):
    try:
        valor = float(input("Digite o valor do saque: "))
        response = requests.post(
            f"{BASE_URL}/saque",
            params={"cpf": cpf, "senha": senha, "valor": valor}
        )
        if response.status_code == 200:
            print(response.json().get("mensagem"))
            print(f"Saldo atual: R${response.json()['saldo']:.2f}")
        else:
            print("Erro:", response.json().get("detail"))
    except ValueError:
        print("Digite um valor válido!")
    except requests.exceptions.RequestException as e:
        print("Erro na conexão:", e)

# Menu principal
while True:
    print("\n===== BANCO ONLINE =====")
    print("1. Criar conta")
    print("2. Login")
    print("3. Sair")
    opcao = input("Escolha (1-3): ")

    if opcao == "1":
        criar_conta()
    elif opcao == "2":
        cpf, senha = login()
        if cpf and senha:
            while True:
                print("\n--- MENU DA CONTA ---")
                print("1. Consultar saldo")
                print("2. Depositar")
                print("3. Sacar")
                print("4. Logout")
                escolha = input("Escolha (1-4): ")

                if escolha == "1":
                    consultar_saldo(cpf, senha)
                elif escolha == "2":
                    realizar_deposito(cpf, senha)
                elif escolha == "3":
                    realizar_saque(cpf, senha)
                elif escolha == "4":
                    print("Logout realizado.")
                    break
                else:
                    print("Opção inválida!")
    elif opcao == "3":
        print("Saindo do cliente...")
        break
    else:
        print("Opção inválida!")
