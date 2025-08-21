 
from pydantic import BaseModel

# Modelo da conta bancária
class Conta(BaseModel):
    cpf: str
    senha: str
    saldo: float = 0.0  # Saldo inicial é 0
