from dotenv import load_dotenv
import os

load_dotenv()

senha = os.getenv("SENHA")

print("Alteração do commit corrigida")

if senha == "1234":
    print("Senha Correta")
else:
    print("Senha Incorreta")