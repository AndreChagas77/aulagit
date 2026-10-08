import os
from dotenv import load_dotenv

load_dotenv()

senha_correta = os.getenv("SENHA")

senhadigitada = input("Digite a senha: ")

if senhadigitada == senha_correta:
    print("Senha Correta")
else:
    print("Senha Incorreta")

print("Olá murillo")
